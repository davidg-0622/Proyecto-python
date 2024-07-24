# __init__.py

from flask import Flask
from afectaciones_coes.config import Config
from afectaciones_coes.extensions import db
from afectaciones_coes import auth, home, add_servicio
from .auth import load_logged_in_user

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialización de SQLAlchemy
    db.init_app(app)

    # Registrar blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(add_servicio.bp)
    
     # Configuración de la aplicación y registros de blueprints
    app.before_request(load_logged_in_user)
    

    return app
