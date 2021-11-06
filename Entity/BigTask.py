from Entity.Task import Task


class BigTask(Task):
    """
    A big task, with subtasks.
    still pretty abstract tho
    """
    def get_progress(self) -> float:
        # return float btwn 0 and 1 that represents how complete this task is.
        pass
    pass
