import os
import hashlib
from flask import Flask, jsonify, request, make_response
import unicodedata 


# sys.setdefaultencoding() does not exist, here!
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

app = Flask(__name__)


@app.route('/')
def hello():
    return 'HelloWorld'


@app.route('/status', methods=['GET'])
def getStatus():
	response = make_response('',201)
	return response

@app.route('/validarFirma', methods=['POST'])
def validar():
	mensaje = request.form['mensaje']
	hash = request.form['hash']
	respuesta = False
	mensaje2=mensaje.upper()
	mensaje3=mensaje2.lower()
	mensaje4=mensaje3.lower()
	h = hashlib.sha256()
	h.update(mensaje)
	
	hashComparar = h.hexdigest()

	if hashComparar.lower() == hash.lower():
		respuesta =True

	respuestaFinal = jsonify({'valido':respuesta,'mensaje':mensaje})
	return respuestaFinal




def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
