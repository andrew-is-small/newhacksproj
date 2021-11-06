class Request:
    """
    Processes request strings, turning it into an object.
    """
    def __init__(self, method, args=[]):
        self.method = method
        self.args = []


def process_request() -> Request:
    """
    processes a request string, returning a request object
    :return:
    """
    # This may change as some methods may take a single argument or something that could contain spaces.
    # like maybe setting title will have only 1 argument
    pass
