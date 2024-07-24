from afectaciones_coes import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))

    def __init__(self, username, email, password, photo=None):
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo

    def __repr__(self):
        return f"User: '{self.username}'"

class Servicio(db.Model):
    __tablename__ = 'servicio'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False)

    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def __repr__(self):
        return f"Servicio: '{self.nombre}'"

class Registrar_afectacion(db.Model):
    __tablename__ = 'registrar_afectacion'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(200), nullable=False)
    numero_ticket = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    fecha_inicio_afectacion = db.Column(db.DateTime, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self,tipo, numero_ticket, descripcion, fecha_inicio_afectacion, hora, id_usuario):
        self.tipo = tipo
        self.numero_ticket = numero_ticket
        self.descripcion = descripcion
        self.fecha_inicio_afectacion = fecha_inicio_afectacion
        self.hora = hora
        self.id_usuario = id_usuario

    def __repr__(self):
        return f"Registrar_afectacion: '{self.numero_ticket}'"
    
    


class Agregar_servicio(db.Model):
    __tablename__ = 'afectacion'
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(200), nullable=False)
    servicio = db.Column(db.String(200), nullable=False)
    tipo_afectacion = db.Column(db.String(200), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)

    def __init__(self,estado, servicio, tipo_afectacion, hora_inicio, hora_fin):
        self.estado = estado
        self.servicio = servicio
        self.tipo_afectacion = tipo_afectacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        

    def __repr__(self):
        return f"Agregar_servicio: '{self.servicio}'"
