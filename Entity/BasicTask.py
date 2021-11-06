from Entity.Task import Task


class BasicTask(Task):
    """
    Basic task. No subtasks, has a title and can be completed.
    """
    def __init__(self):
        super().__init__()

    def complete(self) -> bool:
        self.complete = True

    def is_completed(self) -> bool:
        return self.complete

    def get_due_date(self) -> None: