# test if ids are unique for all different types of tasks
from Entity.RegularTask import RegularTask
from Entity.Task import Task
from Entity.BigTask import BigTask
from Entity.DailyTask import DailyTask
from Entity.ProjectTask import ProjectTask
from Manager.TaskManager import TaskManager


def test_regulartaskmethods():
    task1 = RegularTask("shit on andrew")
    assert task1.is_completed() is False

    task1 = RegularTask("shit on andrew")
    task1.complete()
    assert task1.is_completed() is True

    task1 = RegularTask("shit on andrew")
    task1.complete()
    task1.uncomplete()
    assert task1.is_completed() is False

    task1 = RegularTask("shit on andrew")
    assert task1.title == "shit on andrew"

    task1 = RegularTask("shit on andrew")
    task1.change_title("shit on and")
    assert task1.title == "shit on and"


def test_dailytastmethods():
    daily1 = DailyTask("wee wee andrew", "andeew is gong", "Oct 24 2002")
    daily1.change_title("poodrew")
    assert daily1.title == "poodrew"
    assert daily1.due_date == "poodrew"

    daily1 = DailyTask("wee wee andrew", "andeew is gong", "Oct 24 2002")
    daily1.add_due_date("poodrew")
    assert daily1.title == "poodrew"
    assert daily1.due_date == "poodrew"


def test_dailybigmethods():
    daily1 = DailyTask("wee wee andrew", "andeew is gong", "Oct 24 2002")
    assert daily1.notes == "andeew is gong"
    assert daily1.due_date == "Oct 24 2002"
    assert daily1.subtasks == dict()
    assert daily1.get_progress() == 0
    task_id = daily1.add_subtask("bint")
    assert daily1.get_subtasks()[task_id].get_title() == "bint"
    task_id2 = daily1.add_subtask("bint2")
    assert daily1.get_progress() == 0
    daily1.subtasks[task_id].complete()
    assert daily1.get_progress() == 0.5
    daily1.complete()
    assert daily1.get_progress() == 1
    assert daily1.subtasks[task_id2].is_completed()


def test_dailyremovetask():
    daily1 = DailyTask("wee wee andrew", "andeew is gong", "Oct 24 2002")
    task_id = daily1.add_subtask("bint")
    task_id2 = daily1.add_subtask("bint2")
    assert daily1.subtasks == {task_id: "bint", task_id2: "bint2"}
    daily1.remove_subtask(task_id)
    assert daily1.subtasks == {"task_id": "bint"}


def test_taskmangage():
    taskmanageobj = TaskManager("project", "proj1", "andrew huge ass", "Oct 24")
    assert taskmanageobj.get_due_date == "Oct 24"
    smackid = taskmanageobj.add_subtask("smack andrew")
    assert taskmanageobj.get_subtask(smackid) == "smack andrew"
    assert taskmanageobj.subtasks == {smackid: "smack andrew"}
    assert taskmanageobj.get_progress() == 0
    assert taskmanageobj.complete_subtask(smackid)
    assert taskmanageobj.get_progress() == 1
    assert taskmanageobj.is_completed() is True
    taskmanageobj.remove_subtask(smackid)
    assert taskmanageobj.subtasks == dict()


def test_taskmangage2():
    taskmanageobj = TaskManager("project", "proj1", "andrew huge ass", "Oct 24")
    assert taskmanageobj.get_progress() == 0
    taskmanageobj.complete_task()
    assert taskmanageobj.get_progress() == 1
    smackid = taskmanageobj.add_subtask("smack andrew")
    assert taskmanageobj.get_progress() == 0


if __name__ == "__main__":
    import pytest

    pytest.main(['basic.py'])
