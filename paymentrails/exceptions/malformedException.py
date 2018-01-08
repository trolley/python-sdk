class MalformedException(Exception):
    """
    A Malformed Exception class.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
