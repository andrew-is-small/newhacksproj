class Task:
    """
    Abstract Class
    """

    def __init__(self, title, notes = "", due_date = None):
        self.title = title
        self.notes = notes
        self.complete = False
        self.due_date = due_date

    def complete(self) -> bool:
        pass

    # make sure you throw appropriate exceptions
    def get_title(self) -> str:
        """
        Abstract method
        Returns name of task title
        :return: title as string. If no title return ""
        """
        pass

    def is_completed(self) -> bool:
        """
        Abstract method
        :return: True or false based on whether task is completed
        """
        pass

    def get_notes(self) -> str:
        """
        Abstract method
        :return: notes for the task as a string. If no notes return ""
        """
        pass

    def get_due_date(self) -> None:
        """
        Abstract method
        :return: a date. THINK OF THIS LATER
        """
        pass

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

    def change_title(self) -> None:
        """
        Abstact method
        Mutates title
        :return: None
        """
        pass

    pass
