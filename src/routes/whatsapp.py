from flask import request, Blueprint,jsonify

main = Blueprint('whatsapp', __name__)

@main.route('/', methods=['POST'])
def whatsapp():
    message = request.form.get('Body').lower()
    print(message)
    if message:
        return f'Thank you for your message! A member of our team will be in touch with you soon.'