from typing import Optional

from Commands.TaskCommands import CreateTaskCommand, CreateSubtaskCommand, CompleteTaskCommand, Command, \
    ChangeDateCommand, ChangeTitleCommand, DeleteTaskCommand, SetViewCommand


class CommandConstants:
    def __init__(self):
        self.command_dict = dict()
        self.command_dict['createtask'] = CreateTaskCommand()
        self.command_dict['createsubtask'] = CreateSubtaskCommand()
        self.command_dict['completetask'] = CompleteTaskCommand()
        self.command_dict['changedate'] = ChangeDateCommand()
        self.command_dict['changetitle'] = ChangeTitleCommand()
        self.command_dict['deletetask'] = DeleteTaskCommand()
        self.command_dict['view'] = SetViewCommand()

    def get(self, method: str) -> Optional[Command]:
        if method in self.command_dict:
            return self.command_dict[method]
        return None
