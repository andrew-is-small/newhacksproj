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

    def __init__(self, type, task_id, title="", notes="", due_date=None):
        if type is ProjectTask:
            self.maintask = ProjectTask(task_id, title, notes, due_date)
        if type is DailyTask:
            self.maintask = DailyTask(task_id, title, notes, due_date)

    def add_subtask(self, sub) -> None:
        """
        Adds a subtask to the substask list
        :param sub is a basic task im guessing
        :return: None
        """
        self.maintask.subtasks.append(sub)

    def remove_subtask(self, task_id) -> None:
        """
        Task_id is simply the index
        :param task_id:
        :return:
        """
        self.maintask.subtasks.pop(task_id)

    def get_subtask(self, task_id):
        return self.maintask.subtasks[task_id]

    def complete_subtask(self, task_id) -> None:
        """
        Completes a subtask. You are able to select subtask by id
        :param task_id:
        :return:
        """
        self.maintask.subtasks[task_id].complete

    def complete_task(self) -> None:
        """
        Completes the entire task.
        :return:
        """
        self.maintask.complete

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
