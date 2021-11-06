"""
Commands related to tasks
- creating a task
- deleting a task
- checking a task off.
"""
from typing import Dict


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
        pass


class CreateSubtaskCommand(Command):
    def run(self, args: Dict):
        # get task corresponding to id(in args)
        # create subtasks and append to the shitter
        pass


class CompleteTaskCommand(Command):
    def run(self, args: Dict):
        # get the task
        # run its complete method
        pass
