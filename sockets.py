from flask import Flask,request,render_template, jsonify
from flask_socketio import SocketIO, send
import json
from flask_cors import CORS
from reconocimiento import recorrer

#setup
host='localhost'
port='8585'

app = Flask(__name__)
app.config['SECRET_KEY']="secret!"
socketio = SocketIO(app)
CORS(app)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/send_noti")
def send_noti():
    indice = recorrer()
    if indice == '1':
        msj = json.dumps({"msg":"Autentificacion Correcta", "estado":1})
        socketio.send(msj)
        return msj
    else:
        msj = json.dumps({"msg":"No se reconocio su rostro", "estado":0})
        socketio.send(msj)
        return msj
        

@app.route("/send_noti")
def difundir():
    send(json.dumps({'msj' : 'Envio Correctamente'}))

@socketio.on('connect')
def on_con():
	print("dentrooo")



	


'''
@app.route("/")
def index():
    return "hello Word"

@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)
'''


if __name__ == '__main__':
    socketio.run(app,debug=True,host=host,port=port)
