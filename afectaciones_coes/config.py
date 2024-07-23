SQL = 'mysql://root:123456@localhost:3306/afectaciones_coes'

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = SQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Añade esta línea para evitar advertencias
    CKEDITOR_PKG_TYPE = 'full'
