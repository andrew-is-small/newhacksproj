from Manager.Gettable import Gettable


class TaskManager(Gettable):
    """
    Manages use cases for a BigTask.
    What needs to be done?
    - giving up a title(title of project or the date of the task)
    - checking off a subtask by id
    - reporting its completion/progress
    - setting the date or something idk lol
    - giving up data
    - keeps track of due date.
    """
    def complete_subtask(self, task_id) -> None:
        """
        Completes a subtask. You are able to select subtask by id
        :param task_id:
        :return:
        """
        pass

    def complete_task(self) -> None:
        """
        Completes the entire task.
        :return:
        """
        pass

    def get_basic_data(self):
        """
        Gets the title, completion, progress and due date of the task I guess...
        no idea what the return format is yet.
        :return:
        """
        pass

    def get_data(self):
        """
        Gives all data up
        no idea what the return format is yet.
        :return:
        """
    pass
