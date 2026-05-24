import json

class BaseException(BaseException):
    """
    The Base Exception class.
    """

    def __init__(self, value):
        try:
            BaseException.error_array = json.loads(value)
        except (TypeError, json.JSONDecodeError):
            BaseException.error_array = {"errors": [{"message": value}]}
        self.value = value

    def __str__(self):
        return repr(self.value)
    
    def get_error_array(self):
        return BaseException.error_array["errors"]
