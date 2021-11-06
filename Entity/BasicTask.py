from Entity.Task import Task


class BasicTask(Task):
    """
    Basic task. No subtasks, has a title and can be completed.
    """
    def __init__(self):
        super().__init__()

    def completed(self) -> bool:
        self.completed = True

    def is_completed(self) -> bool:
        return self.completed

    def get_due_date(self) -> None: