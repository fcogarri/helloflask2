import os
import hashlib
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'caca!'

@app.route('/validarFirma', methods=['POST'])
def validar():
	mensaje = request.form['mensaje']
	hash = request.form['hash']
	respuesta = false
	
	h=hashlib.sha256()
	h.update(mensaje)
	hashComparar=h.hexadigest()

	if hashComparar==hash
		respuesta=true;

	respuestaFinal=jsonfiy({'valido:':respuesta, 'mensaje:':mensaje})	
	return respuestaFinal



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
    