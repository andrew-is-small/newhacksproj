from Entity.Task import Task


class RegularTask(Task):
    """
    Basic task. No subtasks, has a title and can be completed.
    """

    def __init__(self, title=""):
        super().__init__(title)
        self.is_complete = False

    def is_completed(self) -> bool:
        return self.is_complete

    def complete(self) -> None:
        self.is_complete = True

    def uncomplete(self) -> None:
        self.is_complete = False

    def get_basic_data(self):
        """
        Gives up its basic data, such as title, progress, completion.
        :return:
        """
        pass

    def get_title(self) -> str:
        return self.title

    def get_data(self):
        """
        Gives up its own data. Do not know the data structure tho.
        :return:
        """
        ret_dict = {
            "title": self.title,
            "completion": self.is_complete,
            "id": self.id
        }
        return ret_dict
