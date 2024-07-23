from afectaciones_coes import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))

    def __init__(self, username, email, password, photo = None):
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo

    def __repr__(self):
        return f"User: '{self.username}'"
    


class Servicio(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False)

    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def __repr__(self):
        return f"Servicio: '{self.nombre}'"