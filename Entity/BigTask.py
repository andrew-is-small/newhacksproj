from typing import List
from Entity.RegularTask import RegularTask
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
        self.is_checked = 0

    def add_subtask(self, title):
        a = RegularTask(title=title)
        self.subtasks[a.id] = a
        return a.id

    def remove_subtask(self, tid) -> bool:
        if tid in self.subtasks:
            self.subtasks.pop(tid)
            return True
        return False

    def get_progress(self) -> float:
        # return float btwn 0 and 1 that represents how complete this task is.
        completed = 0
        if self.subtasks:
            for key in self.subtasks:
                if self.subtasks[key].is_completed():
                    completed += 1
            return completed / len(self.subtasks)
        return self.is_checked

    def get_subtasks(self) -> List[RegularTask]:
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

    def complete(self) -> None:
        self.is_checked = True
        for task in self.subtasks:
            self.subtasks[task].complete()

    def uncomplete(self) -> None:
        self.is_checked = False

    def is_completed(self) -> bool:
        """
        return whether the task is completed if and only if all subtasks are completed
        :return: bool
        """
        for taskies in self.subtasks:
            if not taskies.is_completed:
                return False
        return self.complete
