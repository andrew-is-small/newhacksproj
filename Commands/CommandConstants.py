from typing import Optional

from Commands.TaskCommands import CreateTaskCommand, CreateSubtaskCommand, CompleteTaskCommand, Command


class CommandConstants:
    def __init__(self):
        self.command_dict = dict()
        self.command_dict['createtask'] = CreateTaskCommand()
        self.command_dict['createsubtask'] = CreateSubtaskCommand()
        self.command_dict['completetask'] = CompleteTaskCommand()

    def get(self, method: str) -> Optional[Command]:
        if method in self.command_dict:
            return self.command_dict[method]
        return None
