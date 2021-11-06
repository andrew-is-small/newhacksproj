from typing import List

from Entity.BasicTask import BasicTask
from Entity.BigTask import BigTask


class DailyTask(BigTask):
    """
    Daily tasks. List of daily tasks basically
    """
    def __init__(self):
        super().__init__()
