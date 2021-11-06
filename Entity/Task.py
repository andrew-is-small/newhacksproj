class Task:
    """
    Abstract Class
    """

    def __init__(self, title, notes="", due_date=None):
        self.title = title
        self.notes = notes
        self.complete = False
        self.due_date = due_date

    def completed(self) -> None:
        """
        abstract method
        Mutate self.complete from false to true
        :return: None
        """
        self.complete = True

    def uncompleted(self) -> None:
        """
        abstract method
        Mutate self.complete from true to false
        :return:
        """
        self.complete = False

    # make sure you throw appropriate exceptions
    def get_title(self) -> str:
        """
        Abstract method
        Returns name of task title
        :return: title as string. If no title return ""
        """
        return self.title

    def is_completed(self) -> bool:
        """
        Abstract method
        :return: True or false based on whether task is completed
        """
        return self.complete

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

    def add_due_date(self) -> None:
        """
        Abstract method
        Mutates due_date
        :return: None
        """
        pass

    def add_notes(self) -> None:
        """
        Abstract method
        Mutates notes
        :return: None
        """
        pass

    def change_title(self, newtitle) -> None:
        """
        Abstact method
        Mutates title
        :return: None
        """
        self.title = newtitle

    pass
