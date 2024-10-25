from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.json
    if data and 'message' in data:
        socketio.emit('object_detected', {'message': data['message']})
        return 'Mensaje recibido', 200
    return 'No se recibió ningún mensaje', 400

if __name__ == "__main__":
    socketio.run(app, debug=True)


