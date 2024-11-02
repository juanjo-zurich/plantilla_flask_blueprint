import os
from flask import Flask
from .core import core_bp
from .prueba import prueba_bp
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from dotenv import load_dotenv

from .config.db import db

load_dotenv()
migrate = Migrate()

def crear_app():
    app = Flask(__name__)
    
    
    #Configurar la aplicación Flask con las variables de entorno
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    
    # Registrar Blueprints
    app.register_blueprint(core_bp)
    app.register_blueprint(prueba_bp)
    
    # Configurar proteccion CSRF para formularios
    csrf = CSRFProtect()
    csrf.init_app(app)
    
     # Iniciar database
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    
    #db.init_app(app)
    migrate.init_app(app, db)

    return app