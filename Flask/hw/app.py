from flask import Flask, jsonify

app = Flask(__name__)

frameworks = [
    { "id":1,  "name":"flask" },
    { "id":2,  "name":"ExpressJS" },
    { "id":3,  "name":"Laravel" }
]
@app.route("/")
def index():
    return "Hello World!"

@app.route("/api/frameworks/",methods=["GET"]) # creamos una ruta para nuestra aplicacion 
#el metodo get son las rutas de flask se crean por defecto...  nosotros lo añadimos para ser mas especificos
def get_frameworks():

    return jsonify(frameworks)

@app.route("/api/frameworks/<string:name>")#variables en flask un empoint
def get_framework_by_name(name):
    framework = []
    for f in frameworks:
        if f["name"] == name:
            framework.append(f)
    return jsonify(framework)

if __name__ == "__main__":
    app.run(debug = True) #en flask podemos activar el modo debug
    #el cual nos ayuda editar los archivos que pertenecen a nuestra aplicacion
    #guardarlos y que el servidor detecte esos cambios y se reinicie
