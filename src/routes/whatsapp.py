from flask import request, Blueprint,jsonify

main = Blueprint('whatsapp', __name__)

@main.route('/', methods=['POST'])
def recibe_whatsapp():
    data = 'hola mundo'
    return data
