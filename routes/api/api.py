from flask import Blueprint
from flask import jsonify
from flask import request
from pathlib import Path
from werkzeug.utils import secure_filename
from threading import Thread
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

        file = request.files["file"]

        path = f'{Path().absolute()}/audios/'

        hash : HashInterface = Fac.get_representative(HashInterface)().generate_random_hash()

        filename = f'{hash}{secure_filename(file.filename)}'

        upload_audio_class : UploadAudioRouteInterface = Fac.get_representative(UploadAudioRouteInterface)()

        if filename == '' :
            return jsonify({'message' : 'No file selected'})

        else :

            Conversor : ConversorInterface = Fac.get_representative(ConversorInterface)

            upload_audio_class.save_file(path, filename, file)

            upload_audio_class.start_conversion(Conversor, path, filename)

    return jsonify({
        'message': 'Audio uploaded successfully',
        'hash' : f'{filename}'
        })

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
    response = delete_files_class.delete_files()

    return jsonify(response)