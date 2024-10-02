from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, ping_interval=3, ping_timeout=10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/android')
def android():
    return render_template('android.html')

@socketio.on('connect')
def handle_connect():
    print("Connect")

@socketio.on('disconnect')
def handle_disconnect():
    print("Disconnect")

@socketio.on('text_update')
def handle_text_update(data):
    emit('update_text', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=14150)
