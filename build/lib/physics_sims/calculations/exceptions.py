class TimeInputError(Exception):
    def __init__(self, message="time must be greater then or equal to zero."):
        self.message = message
        super().__init__(message)