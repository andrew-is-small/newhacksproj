from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, send

from Commands.CommandConstants import CommandConstants
from Commands.IdMaker import tid
from Commands.TaskCommands import FetchSortedCommand
from Commands.TaskStorage import TaskStorage
from Entity.Task import Task
from Manager.Derived import Gettable
from Manager.TaskManager import TaskManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
# socketio = SocketIO(app, cors_allowed_origins='*')

print('yo app is shit.')


# initialize task storage
# see this is where we would load a taskstorage if we could but u know...
TASK_STORAGE = TaskStorage()


# we'll do a /<method> post request, that will just make a corresponding command object with method and params
# that will run
# How will we give data to the guy tho wtfff

@app.route('/<method>', methods=['POST'])
def make_request(method):
    # get corresponding command
    try:
        command = CommandConstants().get(method)
        data = request.form
        args = data.to_dict(flat=False)
        # form arguments using arguments passed in.
        output = None
        if command is not None:
            output = command.run(args)
        # output will either be none or json will this work...
        return "" if output is None else output
    except Exception as e:
        return str(e), 404


@app.route('/alldata/<taskid>', methods=['GET'])
def fetch_task(taskid):
    try:
        ts = TaskStorage.get_instance()
        t = ts.get_by_id(taskid)
        # scuffed af
        if isinstance(t, Gettable):
            return t.get_data()
        else:
            return "didn't get none"
    except Exception as e:
        return str(e), 404


@app.route('/basicdata/<taskid>', methods=['GET'])
def fetch_basic(taskid):
    try:
        ts = TaskStorage.get_instance()
        t = ts.get_by_id(taskid)
        # scuffed af
        if isinstance(t, Gettable):
            return t.get_basic_data()
        else:
            return "didn't get none"
    except Exception as e:
        return str(e), 404


@app.route('/fetchall', methods=['GET'])
def fetch_all():
    try:
        fsc = FetchSortedCommand()
        return fsc.run()
    except Exception as e:
        return str(e), 404


if __name__ == "__main__":
    Flask.run(app)
