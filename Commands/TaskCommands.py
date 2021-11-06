"""
Commands related to tasks
- creating a task
- deleting a task
- checking a task off.
"""
from typing import Dict

from Commands.TaskStorage import TaskStorage
from Entity.RegularTask import RegularTask
from Entity.BigTask import BigTask
from Entity.Task import Task
from Manager.TaskManager import TaskManager
from Manager.TaskSorter import sort_tasks

current_task_id = 0


# This technically is Dependency Inversion cuz we rely on Task and BigTask, which are abstract classes uh yeah.
# I am cool.

# task storage
# set it if we have data saved yeah
TASK_STORAGE = TaskStorage.get_instance()


class Command:
    def run(self, args: Dict):
        """
        Runs the command, this is ABSTRACT
        :param args:
        :return:
        """
        pass


# Modifying Commands

class CreateTaskCommand(Command):
    def run(self, args: Dict):
        """
        Creates a new task
        Args requires:
        - type: type of task(project/daily)
        - title(can be empty string)
        - notes(can be empty string)
        - duedate(can be empty string, otherwise formatted datetime string of ONE FORMAT)
        :param args:
        :return:
        """
        # get the single taskStorage object
        ts = TASK_STORAGE

        # create a task
        tm = TaskManager(args['type'], args['title'], args['notes'], args['duedate'])
        # add it to the storage
        ts.add_task(tm)


class CreateSubtaskCommand(Command):
    def run(self, args: Dict):
        """
        Creates a subtasks in a task
        Args requires
        - id(id of the task to create subtask for)
        - title(can be empty string)
        :param args:
        :return:
        """
        ts = TASK_STORAGE
        # get task corresponding to id(in args)
        task = ts.get_by_id(args['id'])
        if isinstance(task, TaskManager):
            task.add_subtask(RegularTask(args['title']))
        # no need to add to storage because it mutates something already in the storage I think


class CompleteTaskCommand(Command):
    def run(self, args: Dict):
        """
        Completes a task.
        Args requires
        - id(id of the task to complete)
        :param args:
        :return:
        """
        # get the task
        ts = TASK_STORAGE
        task = ts.get_by_id(args['id'])
        if isinstance(task, Task):
            # run its complete method
            task.complete()


class ChangeDateCommand(Command):
    def run(self, args: Dict):
        """
        Sets the date of a task
        Args requires:
        - id(id of the task to complete)
        - newdate(formatted date string)
        :param args:
        :return:
        """
        # get the task, change the date
        # get the task
        ts = TASK_STORAGE
        task = ts.get_by_id(args['id'])
        if isinstance(task, BigTask):
            task.add_due_date(args['newdate'])


class ChangeTitleCommand(Command):
    def run(self, args: Dict):
        """
        Changes title of a task
        Args requires:
        - id(id of the task to change)
        - newtitle(new title)
        :param args:
        :return:
        """
        # get the task, change the title
        ts = TASK_STORAGE
        task = ts.get_by_id(args['id'])
        if isinstance(task, Task):
            task.change_title(args['newtitle'])


class DeleteTaskCommand(Command):
    def run(self, args: Dict):
        """
        Deletes a command
        Args requires
        - id(id of the thing to be deleted)
        :param args:
        :return:
        """
        ts = TASK_STORAGE
        ts.delete_task(args["id"])


# Fetching Commands

class FetchSortedCommand(Command):
    def run(self, args: Dict = None):
        """
        Returns a dictionary that maps "project" to a list of projecttask taskmanagers, sorted in order of date.
        Also maps "daily" in the same way
        No args required
        :param args:
        :return:
        """
        # all bigtasks(task manager) should be stored in TaskStorage
        ts = TASK_STORAGE
        ret_dict = dict()
        for key in ts.tasks:
            tm = ts.tasks[key]  # this is a taskmanager
            if tm.task_type not in ret_dict:
                ret_dict[tm.task_type] = [tm]
            else:
                ret_dict[tm.task_type].append(tm)
        for key in ret_dict:
            ret_dict[key] = sort_tasks(ret_dict[key])
        return ret_dict
