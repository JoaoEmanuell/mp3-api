from flask import Blueprint
from flask import jsonify
from flask import request
from pathlib import Path
from werkzeug.utils import secure_filename
from threading import Thread
from json import loads
from urllib.parse import urlparse

from .source import Conversor, Hash

api = Blueprint('api', __name__)

@api.route('/')
def index() :
    return jsonify({'message': 'Welcome to the API'})

@api.route('/upload/', methods=['POST'])
def upload_audio() :
    if request.method == 'POST':
        file = request.files["file"]

        path = f'{Path().absolute()}/audios/'

        hash = Hash.generate_random_hash()

        filename = f'{hash}{secure_filename(file.filename)}'

        if filename == '' :
            return jsonify({'message' : 'No file selected'})

        file.save(f'{path}{filename}')

        Thread(target=Conversor.convert, args=(f'{path}{filename}',)).start()
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

    with open(f'{path}{hash}.json', 'r') as f :
        file = f.read()

        if file == '':
            return jsonify({'status' : False})
        else :
            return jsonify(loads(file))
