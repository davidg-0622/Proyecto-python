from flask import Flask
from afectaciones_coes.config import Config
from afectaciones_coes.extensions import db
from afectaciones_coes import auth, home

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar vistas de home
    app.register_blueprint(home.bp)

    # Registrar vistas de Auth
    app.register_blueprint(auth.bp)

    return app
