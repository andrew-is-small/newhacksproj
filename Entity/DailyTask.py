from typing import List

from Entity.RegularTask import RegularTask
from Entity.BigTask import BigTask


class DailyTask(BigTask):
    """
    Daily tasks. List of daily tasks basically
    """
    def __init__(self, title="", notes="", due_date=""):
        super().__init__(title, notes, due_date)

    def change_title(self, newtitle) -> None:
        """
        Abstact method
        Mutates title
        :return: None
        """
        self.title = newtitle
        self.due_date = newtitle

    def add_due_date(self, date) -> None:
        """
        Abstract method
        Mutates due_date
        :return: None
        """
        self.due_date = date
        self.title = date
