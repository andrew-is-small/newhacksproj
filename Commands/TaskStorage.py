# idk
# we have to make new classes for each type of command, and a command constants shitter yeah
# THIS IS THE CLASS THAT IS GOING TO GET SAVED I GUESS
from typing import Dict

from Manager.TaskManager import TaskManager
from Manager.TaskSorter import sort_tasks


class TaskStorage:
    # WCS, make this not a singleton but just kinda ensure there's only one of them lol
    __instance = None

    @staticmethod
    def get_instance():
        if TaskStorage.__instance is None:
            TaskStorage.__instance = TaskStorage()
        return TaskStorage.__instance

    @staticmethod
    def set_instance(ts):
        if TaskStorage.__instance is None:
            TaskStorage.__instance = ts

    tasks: Dict[str, TaskManager]

    def __init__(self):
        # we're going to map taskManager ids to the actual taskManager
        if self.__instance is not None:
            return
        self.tasks = dict()
        self.current_id = 0
        self.current_viewing = None

    def get_current_viewing(self):
        return self.current_viewing

    def view(self, task_id):
        if task_id in self.tasks:
            self.current_viewing = self.tasks[task_id]
            print("setting viewing page")

    def add_task(self, tm: TaskManager):
        if tm.get_id() not in self.tasks:
            self.tasks[tm.get_id()] = tm

    def delete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks.pop(task_id)
            if self.current_viewing is not None and self.current_viewing.id == task_id:
                self.current_viewing = None
            return
        else:
            for key in self.tasks:
                tm = self.tasks[key]
                if tm.remove_subtask(task_id):
                    return
                # if the thing returns true, we shit on it

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
            a = self.tasks[key]  # a taskManager
            if a.get_subtask(task_id) is not None:
                return a.get_subtask(task_id)
        return None

    def fetch_sorted(self):
        ret_dict = dict()
        for key in self.tasks:
            tm = self.tasks[key]  # this is a taskmanager
            if tm.task_type not in ret_dict:
                ret_dict[tm.task_type] = [tm]
            else:
                ret_dict[tm.task_type].append(tm)
        for key in ret_dict:
            ret_dict[key] = sort_tasks(ret_dict[key])
        return ret_dict
    # I want the capability to return a dict that's like Daily:[id1, id2, ...], Project. These have to be sorted.
    # cuz then we can fetch each of those by id and present them
