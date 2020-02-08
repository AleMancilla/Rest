from flask import Flask, jsonify

app = Flask(__name__)



list_of_objects = [
    { "id": 1, "name":"object 1"},
    { "id": 2, "name":"object 2"},
    { "id": 3, "name":"object 3"}
]

@app.route("/")

def get_all_objects():
    return jsonify(list_of_objects)

if __name__ == "__main__":
    app.run()