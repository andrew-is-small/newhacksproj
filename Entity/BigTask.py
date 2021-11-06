from typing import List
from BasicTask import BasicTask
from Entity.Task import Task


class BigTask(Task):
    """
    Abstract Class
    A big task, with subtasks.
    still pretty abstract tho
    """

    def __init__(self, title="", notes="", due_date=""):
        super().__init__(title)
        self.notes = notes
        self.due_date = due_date
        self.subtasks = dict()

    def add_subtask(self, title):
        a = BasicTask(title=title)
        self.subtasks[a.id] = a

    def get_progress(self) -> float:
        # return float btwn 0 and 1 that represents how complete this task is.
        completed = 0
        for taskies in self.subtasks:
            if taskies.is_completed:
                completed += 1
        return completed / len(self.subtasks)

    def get_subtasks(self) -> List[BasicTask]:
        """
        :return:
        """
        return self.subtasks

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

    def add_notes(self, addednotes) -> None:
        """
        Abstract method
        Mutates notes
        :return: None
        """
        self.notes = addednotes

    def is_completed(self) -> bool:
        """
        return whether the task is completed if and only if all subtasks are completed
        :return: bool
        """
        for taskies in self.subtasks:
            if not taskies.is_completed:
                return False
        return self.complete
