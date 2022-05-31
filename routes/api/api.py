from flask import Blueprint
from flask import jsonify
from flask import request
from pathlib import Path
from json import loads
from urllib.parse import urlparse

from .source import Factory
from .source.interfaces import HashInterface, ConversorInterface

from .source.api_routes_class.interfaces import DeleteFilesRouteInterface, UploadAudioRouteInterface

api = Blueprint('api', __name__)

Fac = Factory()

@api.route('/')
def index() :
    return jsonify({'message': 'Welcome to the API'})

@api.route('/upload/', methods=['POST'])
def upload_audio() :
    if request.method == 'POST':
      
        upload_audio_route : UploadAudioRouteInterface = Fac.get_representative(UploadAudioRouteInterface)()

        upload_audio_route.set_atributes(
            path = f'{Path().absolute()}/audios/',
            file = request.files["file"],
            conversor = Fac.get_representative(ConversorInterface)(),
            hash = Fac.get_representative(HashInterface)(),
        )

        response = upload_audio_route.main()

        return jsonify(response)

@api.route('/converteds/<filename>')
def get_converted_audio(filename : str) :

    url_base = urlparse(request.base_url)[0:2]
    url_base = f'{url_base[0]}://{url_base[1]}'

    return jsonify({
        'audio' : f'{url_base}/static/{filename}', 
        'filename' : f'{filename.rsplit("/")[-1][8:]}'
    })

@api.route('/status/<hash>')
def get_status_file(hash : str) :

    path = f'{Path().absolute()}/status/'
    hash = hash.replace('.mp3', '')

    try : 

        with open(f'{path}{hash}.json', 'r') as f :
            file = f.read()

            if file == '':
                return jsonify({'status' : False})
            else :
                return jsonify(loads(file))

    except FileNotFoundError :
        return jsonify({'status' : False})

@api.route('/delete/<hash>')
def delete_files(hash : str) :
    
    delete_files_class : DeleteFilesRouteInterface = Fac.get_representative(
        DeleteFilesRouteInterface
    )()

    delete_files_class.set_atributes(hash = hash)
    response = delete_files_class.main()

    return jsonify(response)