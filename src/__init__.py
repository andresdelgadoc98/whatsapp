from flask import Flask
from .routes import whatsapp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(whatsapp.main, url_prefix='/wahtsapp')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)