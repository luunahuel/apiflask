
from flask import Flask, jsonify, request

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta GET para la raíz
@app.route('/')
def hello_world():
    return 'BUENAS!! es el Punto de entrada '

# Definir una ruta GET para obtener datos del usuario
@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "115603809"}
    # Obtener parámetros de consulta
    query = request.args.get("query")
    if query:
        user["query"] = query
        return jsonify(user), 200
    return jsonify(user), 200
