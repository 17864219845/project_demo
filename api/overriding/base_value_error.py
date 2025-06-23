class BaseValueError(ValueError):
    message = "unknown"

    def __init__(self, message=None):
        if message is None:
            message = self.message
        super().__init__(message)
