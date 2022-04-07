from flask import Blueprint
from flask import jsonify

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return jsonify({'message': 'Welcome to the API'})