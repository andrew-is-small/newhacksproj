from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

print('yo app is shit.')
# we'll do a /<method> post request, that will just make a corresponding command object with method and params
# that will run
