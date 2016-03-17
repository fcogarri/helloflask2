import os
import hashlib
from flask import Flask, jsonify, request
import unicodedata 

app = Flask(__name__)


@app.route('/')
def hello():
    return 'HelloWorld'


@app.route('/status', methods=['GET'])
def validar():
	hola='a'
	return render_template('status.html'), 201

@app.route('/validarFirma', methods=['POST'])
def validar():
	mensaje = request.form['mensaje']
	hash = request.form['hash']
	respuesta = 'Falso'
	mensaje2=remove_accents(mensaje)

	h = hashlib.sha256()
	h.update(mensaje2)
	hashComparar = h.hexdigest()

	if hashComparar.lower() == hash.lower():
		respuesta ='True'

	respuestaFinal = jsonify({'valido:':respuesta, 'mensaje:':mensaje,'hashReal:':hash,'hashCalculado:':hashComparar})
	return respuestaFinal




def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
