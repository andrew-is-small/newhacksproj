from Entity.Task import Task


class BasicTask(Task):
    """
    Basic task. No subtasks, has a title and can be completed.
    """

    def __init__(self, title=""):
        super().__init__(title)

    def is_completed(self) -> bool:
        return super().completed
