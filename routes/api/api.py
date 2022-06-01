from flask import Blueprint
from flask import jsonify
from flask import request
from pathlib import Path
from json import loads

from .source import Factory
from .source.interfaces import HashInterface, ConversorInterface

from .source.api_routes_class.interfaces import DeleteFilesRouteInterface, UploadAudioRouteInterface, GetConvertedAudioRouteInterface, GetStatusFileRouteInterface

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

    get_converted_audio_route : GetConvertedAudioRouteInterface = Fac.get_representative(GetConvertedAudioRouteInterface)()
    get_converted_audio_route.set_atributes(
        filename = filename,
        url_base = request.base_url
    )

    response = get_converted_audio_route.main()

    return jsonify(response)

@api.route('/status/<hash>')
def get_status_file(hash : str) :

    '''

    try : 

        with open(f'{path}{hash}.json', 'r') as f :
            file = f.read()

            if file == '':
                return jsonify({'status' : False})
            else :
                return jsonify(loads(file))

    except FileNotFoundError :
        return jsonify({'status' : False})'''

    get_status_file_route : GetStatusFileRouteInterface = Fac.get_representative(GetStatusFileRouteInterface)()
    get_status_file_route.set_atributes(
        path = f'{Path().absolute()}/status/',
        hash = hash
    )

    response = get_status_file_route.main()

    return jsonify(response)

@api.route('/delete/<hash>')
def delete_files(hash : str) :
    
    delete_files_class : DeleteFilesRouteInterface = Fac.get_representative(
        DeleteFilesRouteInterface
    )()

    delete_files_class.set_atributes(hash = hash)
    response = delete_files_class.main()

    return jsonify(response)