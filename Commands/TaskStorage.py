# idk
# we have to make new classes for each type of command, and a command constants shitter yeah
# THIS IS THE CLASS THAT IS GOING TO GET SAVED I GUESS
from typing import Dict

from Manager.TaskManager import TaskManager


class TaskStorage:
    # WCS, make this not a singleton but just kinda ensure there's only one of them lol

    tasks: Dict[TaskManager]

    def __init__(self):
        # we're going to map taskManager ids to the actual taskManager
        self.tasks = dict()
        self.current_id = 0

    def add_task(self, tm: TaskManager):
        if tm.get_id() not in self.tasks:
            self.tasks[tm.get_id()] = tm

    def get_by_id(self, task_id):
        """
        Gets a task by task_id. Looks inside all tasks and subtasks.
        Returns either a taskManager, or a BasicTask
        :param task_id:
        :return:
        """
        # will look at each taskmanager, and also tasks inside each taskmanager
        if task_id in self.tasks:
            return self.tasks[task_id]
        for key in self.tasks:
            a = self.tasks[key] # a taskManager
            if a.get_subtask(task_id) is not None:
                return a.get_subtask(task_id)
        return None
    # I want the capability to return a dict that's like Daily:[id1, id2, ...], Project. These have to be sorted.
    # cuz then we can fetch each of those by id and present them
