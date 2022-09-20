from typing import Optional


class DatabaseException(Exception):
    """Custom Exception class for Database exceptions."""
    def __init__(self, message: Optional[str] = 'An error occurred in DataBase', description: Optional[str] = None):
        """
        Args:
            message (str): optional arg, displaying message for exception.
            description (str): optional arg, displaying more detailed description of the exception.
        """
        super(DatabaseException, self).__init__(message)
        self.description = description
        self.message = message
