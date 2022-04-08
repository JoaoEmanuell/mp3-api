from flask import Blueprint
from flask import jsonify
from flask import request
from pathlib import Path
from werkzeug.utils import secure_filename
from threading import Thread
from os import environ

from .source import Conversor

api = Blueprint('api', __name__)

@api.route('/')
def index() :
    return jsonify({'message': 'Welcome to the API'})

@api.route('/upload/', methods=['POST'])
def upload_audio() :
    if request.method == 'POST':
        for file in request.files.getlist("file"): # getlist["file"] retorna uma lista que contem os arquivos, enviados.
            file.save(f'{Path().absolute()}/audios/{secure_filename(file.filename)}')
        Thread(target=Conversor.convert, args=(f'{Path().absolute()}/audios/{secure_filename(file.filename)}',)).start()
    return {'message': 'Audio uploaded successfully'}

@api.route('/converteds/<filename>')
def get_converted_audio(filename) :
    if environ['FLASK_ENV'] == 'prod' :
        return f'<audio controls src="/static/{filename}"></audio>'
    else : 
        return jsonify({'audio' : f'http://127.0.0.1:5000/static/{filename}'})