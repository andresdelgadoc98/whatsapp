from flask import request, Blueprint,jsonify
from twilio.twiml.messaging_response import MessagingResponse

main = Blueprint('whatsapp', __name__)



@main.route('/', methods=['POST'])
def whatsapp():
    """Respond to incoming calls with a simple text message."""
    msg = request.form.get('Body')
    print(msg)
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)
