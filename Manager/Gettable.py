class Gettable:
    """
    A class that is able to give its information to the frontend
    Data type of the info is not decided yet.
    """

    def get_basic_data(self):
        """
        Gives up its basic data, such as title, progress, completion.
        This is an ABSTRACT method and needs to be implemented by derived classes.
        :return:
        """
        pass

    def get_data(self):
        """
        Gives up its own data. Do not know the data structure tho.
        This is an ABSTRACT method and needs to be implemented by derived classes.
        :return:
        """
        pass
