from Entity.BigTask import BigTask


class ProjectTask(BigTask):
    """
    A project, with subtasks and shit
    """

    def __init__(self, title="", notes="", due_date=""):
        super().__init__(title, notes, due_date)


