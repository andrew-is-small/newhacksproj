from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send

from Commands.CommandConstants import CommandConstants

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
# socketio = SocketIO(app, cors_allowed_origins='*')

print('yo app is shit.')


# initialize task storage

# we'll do a /<method> post request, that will just make a corresponding command object with method and params
# that will run

@app.route('/<method>', methods=['POST'])
def make_request(method):
    # get corresponding command
    command = CommandConstants().get(method)
    if command is not None:
        command.run()
