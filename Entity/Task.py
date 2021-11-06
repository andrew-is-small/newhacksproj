import uuid


class Task:
    """
    Abstract Class
    No due dates and notes for basic tasks
    """

    def __init__(self, title=""):
        self.title = title
        self.complete = False
        self.id = uuid.uuid4()

    def complete(self) -> None:
        """
        abstract method
        Mutate self.complete from false to true
        :return: None
        """
        self.complete = True

    def uncomplete(self) -> None:
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
        pass

    def change_title(self, newtitle) -> None:
        """
        Abstact method
        Mutates title
        :return: None
        """
        self.title = newtitle
