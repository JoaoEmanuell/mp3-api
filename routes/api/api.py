from flask import Blueprint
from flask import jsonify
from flask import request
from pathlib import Path
from werkzeug.utils import secure_filename

api = Blueprint('api', __name__)

@api.route('/')
def index() :
    return jsonify({'message': 'Welcome to the API'})

@api.route('/upload/', methods=['POST'])
def upload_audio() :
    if request.method == 'POST':
        for file in request.files.getlist("file"): # getlist["file"] retorna uma lista que contem os arquivos, enviados.
            file.save(f'{Path().absolute()}/audios/{secure_filename(file.filename)}')
    return {'message': 'Audio uploaded successfully'}