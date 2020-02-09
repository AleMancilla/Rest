from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

#necesitamos un conector y una ruta absoluta para la base de datos#
BASE_DIR = os.path.abspath(os.path.dirname(__file__))#ruta absoluta
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db") #

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI #este no debe faltar
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
db = SQLAlchemy(app) 

class Framework(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    #name = db.Colum(db.String(50), nullable = False , unique = True)
    name = db.Column(db.String(50))
    

@app.route("/")
def index():
    return "Hello World! dbs"

