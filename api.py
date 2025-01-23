
from flask import Flask, jsonify, request

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta GET para la raíz
@app.route('/')
def hello_world():
    return 'Hello!'
