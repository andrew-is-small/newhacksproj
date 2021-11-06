# idk
# we have to make new classes for each type of command, and a command constants shitter yeah
# THIS IS THE CLASS THAT IS GOING TO GET SAVED I GUESS
import Commands.TaskStorage
from Manager.TaskManager import TaskManager


class TaskStorage:
    __instance = None

    @staticmethod
    def get_instance():
        if TaskStorage.__instance is None:
            TaskStorage.__instance = TaskStorage()
        return TaskStorage.__instance

    @staticmethod
    def set_instance(ts: Commands.TaskStorage.TaskStorage):
        # idk if this will work tbh
        if TaskStorage.__instance is None:
            TaskStorage.__instance = ts

    def __init__(self):
        # we're going to map taskManager ids to the actual taskManager
        if TaskStorage.__instance is not None:
            return
        self.tasks = dict()
        self.current_id = 0

    def add(self, data):
        task_id = self.current_id
        self.current_id += 1
        pass

    def get(self, task_id):
        # will look at each taskmanager, and also tasks inside each taskmanager
        pass

    def get_id(self):
        current_id = self.current_id
        self.current_id += 1
        return current_id
