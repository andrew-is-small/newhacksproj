from Entity.Task import Task


class RegularTask(Task):
    """
    Basic task. No subtasks, has a title and can be completed.
    """

    def __init__(self, title=""):
        super().__init__(title)

    def is_completed(self) -> bool:
        return super().completed()

    def get_basic_data(self):
        """
        Gives up its basic data, such as title, progress, completion.
        :return:
        """
        pass

    def get_data(self):
        """
        Gives up its own data. Do not know the data structure tho.
        :return:
        """
        pass
