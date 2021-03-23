from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#Create database for all notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000)) #Notes cannot be more than 10,000 characters long
    date = db.Column(db.DateTime(timezone = True), default =func.now()) #grabs current date and time whenever note is created and adds to database
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Creates One to Many relationship: one use can have many notes. FOREIGN KEY


#Create the database for all users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True) #Invalid to create a user that already exists
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #Gives access to all noted from a user when clicked upon
