from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initilization the data base 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'registration_form'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #Connects the flask app to my database 
    db.init_app(app)

    from .views import views
    app.register_blueprint(views)

    with app.app_context():
        db.create_all()
    
    return app

