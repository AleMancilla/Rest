from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields 
# marshmellow nos ayudara 

import os

#necesitamos un conector y una ruta absoluta para la base de datos#
BASE_DIR = os.path.abspath(os.path.dirname(__file__))#ruta absoluta
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db") #

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI #este no debe faltar
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
db = SQLAlchemy(app) 

class Framework(db.Model):
    __tablename__ = "frameworks" # solo por cuestiones de semanticas para llamarle a la tabla framewors ya que antes se llamaba framework
    id = db.Column(db.Integer, primary_key = True)
    #name = db.Colum(db.String(50), nullable = False , unique = True)
    name = db.Column(db.String(300))

# serializar un objeto de alto nivel a bajo nivel como diccionario
class FrameworkSchema(Schema):
    id = fields.Int()
    name = fields.Str()

@app.route("/")
def index():
    return "Hello World! dbs"

@app.route("/api/frameworks/<string:name>", methods = ["GET"])
def get_one_framework_by_name(name):
    framework = Framework.query.filter_by(name=name).first()
    framework_schema = FrameworkSchema()
    result = framework_schema.dump(framework)# pasamos el objeto que queremos serializar

    return jsonify(result)

@app.route("/api/frameworks/")
def get_all_frameworks():
    frameworks = Framework.query.all()
    framework_schema = FrameworkSchema(many = True)
    result = framework_schema.dump(frameworks)

    return jsonify(result)

#construir nuestra rest de api
@app.route("/api/frameworks/", methods=["POST"])
def add_framework():
    new_framework = Framework(name=request.json["name"])
    db.session.add(new_framework)
    db.session.commit()

    framework_dict = {
        "id": new_framework.id,
        "name": new_framework.name
    }
    #return jsonify(new_framework)# jsonify no puede convertir objetos a formato json
    return jsonify(framework_dict)

@app.route("/api/frameworks/<int:id>", methods = ["PUT"])
def edit_framework(id):
    framework = Framework.query.filter_by(id=id).first() # consuta donde especificamos un filtro
    framework.name = request.json["name"]

    db.session.commit()

    framework_dict = dict(id = framework.id, name = framework.name)
    # otra forma de hacer diccionario en python
    # equivale a 
    # framework_dict = {
    #     "id": new_framework.id,
    #     "name": new_framework.name
    # }
    return jsonify(framework_dict)


@app.route("/api/frameworks/<int:id>", methods = ["DELETE"])
def delete_framework(id):
    framework = Framework.query.get(id) # consulta solo funciona para el id
    db.session.delete(framework)
    db.session.commit()

    return jsonify({"message":"ok"})




