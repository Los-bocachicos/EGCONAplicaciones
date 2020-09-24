from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.Aplicaciones import Aplicacion

app = Flask(__name__)
CORS(app)


@app.route('/aplicaciones', methods=['GET'])
def obtenerAplicaciones():
    return Aplicacion.listarAplicaciones()


@app.route('/aplicaciones', methods=['POST'])
def agregarAplicacion():
    body = request.json
    print(body)
    return Aplicacion.crearAplicacion(body)


@app.route('/aplicaciones/<idAplicacion>/', methods=['PUT'])
def actualizarAplicacion(idAplicacion):
    body = request.json
    return Aplicacion.actualizarAplicacion(idAplicacion, body)


@app.route('/aplicaciones/<idAplicacion>/', methods=['DELETE'])
def eliminarAplicacion(idAplicacion):
    return Aplicacion.eliminarAplicacion(idAplicacion)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
