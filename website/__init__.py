from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#create database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'svsffgf dfjwisf sdjfh'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #take defined database and tell it what app we are going to use
    db.init_app(app)


    #import urls from views and auth
    from .views import views
    from .auth import auth

    #Create no prefix in URLs
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #Tells Flask how to load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #Looks for primary key
    
    return app

#Create function to check for database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
