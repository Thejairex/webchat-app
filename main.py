from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] == 'secret!'

socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/chat')
def chat():
	return render_template('chat.html')

@socketio.on('connect')
def handle_connect():
    print('Se ha conectado un nuevo cliente.')

@socketio.on('disconnect')
def handle_disconnect():
    print('Se ha desconectado un cliente.')

@socketio.on('chat_message')
def handle_chat_message(message):
    print('Mensaje recibido:', message)
    emit('chat_message', message, broadcast=True)
    

if __name__ == '__main__':
	app.run(debug=True)