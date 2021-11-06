from Manager.Gettable import Gettable
from Manager.Derived import Gettable, Saveable


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
    def __init__(self, type, title="", notes="", due_date=None):
        if self.type is ProjectTask:
            self.maintask = ProjectTask(title, notes, due_date)
        if self.type is DailyTask:
            self.maintask = DailyTask(title, notes, due_date)

    def add_subtask(self):

    def remove_subtask(self, task_id):
        
    def get_subtask(self, task_id):

    def complete_subtask(self, task_id) -> None:
        """
        Completes a subtask. You are able to select subtask by id
        :param task_id:
        :return:
        """
        pass

    def complete_task(self) -> None:
        """
        Completes the entire task.
        :return:
        """
        pass

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
    pass
