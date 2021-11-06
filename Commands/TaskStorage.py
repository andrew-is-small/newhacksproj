# idk
# we have to make new classes for each type of command, and a command constants shitter yeah
# THIS IS THE CLASS THAT IS GOING TO GET SAVED I GUESS
from Manager.TaskManager import TaskManager


class TaskStorage:
    def __init__(self):
        # we're going to map taskManager ids to the actual taskManager
        self.tasks = dict()

    def add(self, tm: TaskManager):
        pass

    def get(self, task_id):
        # will look at each taskmanager, and also tasks inside each taskmanager
        pass
