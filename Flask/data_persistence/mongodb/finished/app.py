from flask import Flask, jsonify, request
from flask_mongoalchemy import MongoAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
#establecemos la coneccion con la base de datos
app.config["MONGOALCHEMY_DATABASE"]="restapiscourse"
#############
db = MongoAlchemy(app)

class Framework(db.Document):
    #id es tan importante que ya esta implicito por defecto
    name = db.StringField()

class FrameworkSchema(Schema):
    id = fields.Str(attribute = "mongo_id") # mongo_id asi se espera ese atributo y se asigna a id
    name = fields.Str()


@app.route("/")
def index():
    return "Hello World! mongoDB"

# GET METHOD
@app.route("/api/frameworks/", methods=["GET"])
def get_frameworks():

    return jsonify(results)

@app.route("/api/frameworks/<string:name>", methods = ["GET"])
def get_frameworks_by_name(name):
    framework = Framework.query.filter(Framework.name == name).first()
    framework_schema = FrameworkSchema()
    results = framework_schema.dump(framework)
    return jsonify(results)


# POST METHOD
@app.route("/api/frameworks/",methods=["POST"])
def add_framework():

    new_framework = Framework(name = request.json["name"])
    new_framework.save()
    
    framework_dict = {
        "id":"{}".format(new_framework.mongo_id),
        "name":new_framework.name
    }

    return jsonify(framework_dict)

# PUT METHOD
@app.route("/api/frameworks/<string:id>", methods=["PUT"])
def edit_framework(id):
    framework = Framework.query.get(id) #recuperar el framework
    framework.name = request.json["name"] # accedemos a cada uno de sus atributos en este caso el nombre
    framework.save() #una vez echo los cambios lo guardamos

    framework_dic = {
        "id": f"{framework.mongo_id}",
        "name":framework.name
    }

    return jsonify(framework_dic)

# DELETE METHOD
@app.route("/api/frameworks/<string:id>", methods = ["DELETE"])
def delete_framework(id):
    framework = Framework.query.get(id)
    framework.remove()

    return jsonify({"Message":"ok"})