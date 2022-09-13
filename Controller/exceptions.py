from typing import Optional


class DatabaseException(Exception):
    def __init__(self, message: Optional[str] = 'This is illegal move', description: Optional[str] = None):
        super(DatabaseException, self).__init__(message)
        self.description = description
        self.message = message
