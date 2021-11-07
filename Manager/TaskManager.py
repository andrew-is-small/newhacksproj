from Manager.Derived import Gettable, Saveable
from Entity.ProjectTask import ProjectTask
from Entity.DailyTask import DailyTask


class TaskManager(Gettable, Saveable):
    """
    Manages use cases for a BigTask.
    What needs to be done?
    - giving up a title(title of project or the date of the task)
    - checking off a subtask by id
    - reporting its completion/progress
    - setting the date or something idk lol
    - giving up data
    - keeps track of due date.
    """

    def __init__(self, task_type, title="", notes="", due_date=None):
        self.task_type = task_type
        if task_type == "project":
            self.maintask = ProjectTask(title, notes, due_date)
        if task_type == "daily":
            self.maintask = DailyTask(title, notes, due_date)
        self.id = self.get_id()

    def __str__(self):
        return "[TM]" + self.maintask.title

    def get_title(self):
        return self.maintask.get_title()

    def get_due_date(self):
        return self.maintask.due_date

    def add_subtask(self, title) -> str:
        """
        Adds a subtask to the substask list
        :param title:
        :return: None
        """
        return self.maintask.add_subtask(title)

    def remove_subtask(self, task_id) -> bool:
        """
        Task_id is simply the index
        :param task_id:
        :return: if we removed anything
        """
        return self.maintask.remove_subtask(task_id)

    def get_subtask(self, task_id):
        return self.maintask.subtasks[task_id]

    def complete_subtask(self, task_id) -> None:
        """
        Completes a subtask. You are able to select subtask by id
        :param task_id:
        :return:
        """
        self.maintask.subtasks[task_id].complete()

    def complete_task(self) -> None:
        """
        Completes the entire task.
        :return:
        """
        self.maintask.complete()

    def get_progress(self) -> int:
        return self.maintask.get_progress()

    def get_basic_data(self):
        """
        Gets the title, completion, progress and due date of the task I guess...
        no idea what the return format is yet.
        :return:
        """
        pass

    def get_data(self):
        """
        Gives all data up
        no idea what the return format is yet.
        :return:
        """
        ret_dict = dict()
        ret_dict['title'] = self.get_title()
        ret_dict['id'] = self.get_id()
        ret_dict['duedate'] = self.maintask.due_date
        ret_dict['progress'] = str(float(self.get_progress())*100)
        ret_dict['subtasks'] = []
        for task in self.maintask.get_subtasks():
            ret_dict['subtasks'].append(task.title)
        return ret_dict

    def get_id(self):
        return self.maintask.id

