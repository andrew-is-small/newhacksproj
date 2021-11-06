# test if ids are unique for all different types of tasks
from Entity.RegularTask import RegularTask
from Entity.Task import Task
from Entity.BigTask import BigTask
from Entity.DailyTask import DailyTask
from Entity.ProjectTask import ProjectTask


def test_1():
    task1 = RegularTask("shit on andrew")
    assert task1.is_completed() is False

    task1 = RegularTask("shit on andrew")
    task1.complete()
    assert task1.is_completed() is True


if __name__ == "__main__":
    import pytest

    pytest.main(['basic.py'])
