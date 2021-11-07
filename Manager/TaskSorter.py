from typing import List

from Entity.BigTask import BigTask
from Entity.Task import Task
from Manager.TaskManager import TaskManager


def sort_tasks(lst: List[TaskManager]) -> List[TaskManager]:
    """
    Sorts tasks by due date, returns a list of ids of the tasks by due date.
    """
    # this might be faulty if some shitters have dates and some don't but yeah.
    lst2 = sorted(lst, key=lambda taskmanager: taskmanager.get_due_date(), reverse=True)
    # ret_lst = []
    # for a in lst2:
    #     ret_lst.append(a.get_id())
    return lst2
