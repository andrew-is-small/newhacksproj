from typing import List
from BasicTask import BasicTask
from Entity.Task import Task


class BigTask(Task):
    """
    Abstract Class
    A big task, with subtasks.
    still pretty abstract tho
    """

    def __init__(self, title, notes="", due_date=None):
        self.title = title
        self.notes = notes
        self.complete = False
        self.due_date = due_date
        self.subtasks = []
        super().__init__()

    def get_progress(self) -> float:
        # return float btwn 0 and 1 that represents how complete this task is.
        pass

    def get_subtasks(self) -> List[BasicTask]:
        """
        :return:
        """
        pass

    def get_notes(self) -> str:
        """
        Abstract method
        :return: notes for the task as a string. If no notes return ""
        """
        return self.notes

    def get_due_date(self) -> None:
        """
        Abstract method
        :return: a date. THINK OF THIS LATER
        """
        return self.due_date

    def add_due_date(self, date) -> None:
        """
        Abstract method
        Mutates due_date
        :return: None
        """
        self.due_date = date

    def add_notes(self) -> None:
        """
        Abstract method
        Mutates notes
        :return: None
        """
        pass

    def is_completed(self) -> bool:
        pass
