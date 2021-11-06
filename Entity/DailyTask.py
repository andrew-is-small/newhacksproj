from typing import List

from Entity.BasicTask import BasicTask
from Entity.BigTask import BigTask


class DailyTask(BigTask):
    """
    Daily tasks. List of daily tasks basically
    """
    subtasks: List[BasicTask]

    pass
