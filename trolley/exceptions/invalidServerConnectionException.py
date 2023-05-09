from trolley.exceptions.baseException import BaseException

class InvalidServerConnectionException(BaseException):
    """
    An Invalid Field Exception class.
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def __str__(self):
        return repr(self.value)
