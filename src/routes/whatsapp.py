from flask import request, Blueprint,jsonify

main = Blueprint('whatsapp', __name__)

@main.route('/', methods=['POST'])
def recibe_whatsapp():
    data = request.form  # Twilio envía los datos en request.form
    mensaje = data.get('Body', 'No message received')  # Obtiene el mensaje del usuario
    print(f"Mensaje recibido: {mensaje}")  # Imprime en la consola
    return "Mensaje recibido"  # Respuesta al webhook de Twilio