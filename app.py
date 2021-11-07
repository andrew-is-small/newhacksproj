from flask import Flask, request, send_from_directory, render_template, redirect, url_for

from Commands.CommandConstants import CommandConstants
from Commands.TaskCommands import FetchSortedCommand
from Commands.TaskStorage import TaskStorage
from Manager.Derived import Gettable
from Manager.TaskManager import TaskManager

# TODO fix delete, make the ability to make new tasks or something
# TODO fix subtasks
# TODO make ability to check off subtasks

app = Flask(__name__, template_folder="pages")
app.config['SECRET_KEY'] = 'mysecret'
# socketio = SocketIO(app, cors_allowed_origins='*')

print('yo app is shit.')

# initialize task storage
# see this is where we would load a taskstorage if we could but u know...
TaskStorage.set_instance(TaskStorage())
TASK_STORAGE = TaskStorage.get_instance()


def generate_random_tasks():
    task1 = TaskManager("project", "make a sandwich", due_date="11/07")
    task2 = TaskManager("daily", "eat lunch", due_date="11/07")
    task1_id = task1.get_id()
    TASK_STORAGE.add_task(task1)
    TASK_STORAGE.add_task(task2)


generate_random_tasks()


def render_page():
    dic = TASK_STORAGE.fetch_sorted()
    project, daily = [], []
    if "project" in dic:
        project = dic["project"]
    if "daily" in dic:
        daily = dic["daily"]

    current_viewing = TASK_STORAGE.get_current_viewing()
    for i in range(0, len(project)):
        project[i] = project[i].get_data()
    for i in range(0, len(daily)):
        daily[i] = daily[i].get_data()

    if current_viewing is None:
        current_viewing = {
            "title": "None",
            "id": "",
            "progress": "0",
            "subtasks": []
        }
    else:
        current_viewing = current_viewing.get_data()
    return render_template('index2.html', current_viewing=current_viewing, projects=project, daily=daily)

    # I need basic info[TITLE/DATE] for sidebar tasks + links to setViewing
    # I need full info for the viewingTask


# we'll do a /<method> post request, that will just make a corresponding command object with method and params
# that will run
# How will we give data to the guy tho wtfff

# basic page getter methods
@app.route('/')
@app.route('/index')
def get_page():
    # dic = TASK_STORAGE.fetch_sorted()
    # project, daily = [], []
    # if "project" in dic:
    #     project = dic["project"]
    #     print("found project", project)
    # if "daily" in dic:
    #     daily = dic["daily"]
    #     print("found daily", daily)
    # return render_template('index.html', projects=project, daily=daily)
    print("rendering page!!")
    return render_page()


@app.route('/<path:path>')
def get_resource(path):
    print(path)
    return send_from_directory('pages', path)


# command methods

@app.route('/cmd/<method>', methods=['GET'])
def make_request(method):
    # get corresponding command
    print("received command", method)
    try:
        command = CommandConstants().get(method)
        data = request.args
        args = data.to_dict(flat=True)
        print("got args", args)
        # form arguments using arguments passed in.
        output = None
        if command is not None:
            output = command.run(args)
        # output will either be none or json will this work...
    except Exception as e:
        print("make_request failed, " + str(e))
    finally:
        return redirect(url_for('get_page'))


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
