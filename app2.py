import os
import hashlib
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'HelloWorld'

@app.route('/validarFirma', methods=['POST'])
def validar():
	mensaje = request.form['mensaje']
	hash = request.form['hash']
	respuesta = False

	h = hashlib.sha256()
	h.update(mensaje)
	hashComparar = h.hexdigest()

	if hashComparar == hash:
		respuesta =True

	respuestaFinal = jsonify({'valido:':respuesta, 'mensaje:':mensaje})
	return respuestaFinal



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
