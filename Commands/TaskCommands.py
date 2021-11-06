"""
Commands related to tasks
- creating a task
- deleting a task
- checking a task off.
"""
from typing import Dict

current_task_id = 0


class Command:
    def run(self, args: Dict):
        """
        Runs the command, this is ABSTRACT
        :param args:
        :return:
        """
        pass


class CreateTaskCommand(Command):
    def run(self, args: Dict):
        # create a task
        # add it to the storage
        pass


class CreateSubtaskCommand(Command):
    def run(self, args: Dict):
        # get task corresponding to id(in args)
        # create subtask and append to the shitter
        # no need to add to storage
        pass


class CompleteTaskCommand(Command):
    def run(self, args: Dict):
        # get the task
        # run its complete method
        pass


class ChangeDateCommand(Command):
    def run(self, args: Dict):
        # get the task, change the date
        pass


class ChangeTitleCommand(Command):
    def run(self, args: Dict):
        # get the task, change the title
        pass
