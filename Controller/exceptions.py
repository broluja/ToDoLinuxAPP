"""Custom exceptions used in this app"""
import json
import traceback
from datetime import datetime, timezone
import logging


class BaseAPPException(Exception):  # Level 1 exception
    """Generic APP exception"""
    internal_error_message = 'APP error occurred.'
    user_error_message = 'Something went wrong. An unexpected error occurred on our end.'
    status = 'APP Error'

    def __init__(self, *args, user_message=None):
        if args:
            self.internal_error_message = args[0]
            super(BaseAPPException, self).__init__(*args)
        else:
            super(BaseAPPException, self).__init__(self.internal_error_message)
        if user_message is not None:
            self.user_error_message = user_message
        self.logger = logging.getLogger()
        self.set_logger()

    @property
    def traceback(self):
        return traceback.TracebackException.from_exception(self).format()

    def set_logger(self):
        ch = logging.FileHandler(filename='exceptions.log')
        ch.setLevel(logging.WARNING)
        self.logger.addHandler(ch)

    def to_json(self):
        err_object = {'status': self.status, 'message': self.user_error_message}
        return json.dumps(err_object)

    def to_log(self):
        exception = {
            'type': type(self).__name__,
            'status': self.status,
            'message': self.args[0] if self.args else self.internal_error_message,
            'args': self.args[1:],
            'traceback': list(self.traceback)
        }
        self.logger.warning(f'EXCEPTION: {datetime.now(timezone.utc).isoformat()}: {exception}')


class APIException(BaseAPPException):  # Level 2 exception
    """Generic API exception"""
    internal_error_message = 'API error occurred.'
    user_error_message = 'Something went wrong. An unexpected error occurred on our end.'
    status = 'API Error.'


class CallLimitReachedException(APIException):
    """Returned when minute/monthly limit is reached."""
    internal_error_message = 'API error occurred. Access to data failed.'
    user_error_message = 'You have reached minute/monthly limit.'
    status = 'API Error - status limit reached.'


class ApiKeyExpiredException(APIException):
    """Returned when API key is expired."""
    internal_error_message = 'API error occurred. Access to data failed.'
    user_error_message = 'Your subscription has expired.'
    status = 'API Error - api key expired.'


class IncorrectApiKeyException(APIException):
    """Returned when using wrong API key."""
    internal_error_message = 'API error occurred. Access to data failed.'
    user_error_message = 'Invalid API key.'
    status = 'API Error - invalid api key.'


class IpLocationFailedException(APIException):
    """Returned when service is unable to locate IP address of request."""
    internal_error_message = 'API error occurred. Access to data failed.'
    user_error_message = 'Sorry, we are unable to locate your IP.'
    status = 'API Error - Unable to locate IP.'


class NoNearestLocationException(APIException):
    """Returned when there is no nearest station within specified radius."""
    internal_error_message = 'API error occurred. Access to data failed.'
    user_error_message = 'Sorry, we are unable to locate nearest station.'
    status = 'API Error - Unable to locate nearest station.'


class FeatureNotAvailableException(APIException):
    """Returned when call requests a feature that is not available in chosen subscription plan."""
    internal_error_message = 'API error occurred. Access to data failed.'
    user_error_message = 'Sorry, your subscription does not cover this feature.'
    status = 'API Error - Not available in this subscription plan.'


class TooManyRequestsException(APIException):
    """Returned when more than 10 calls per second are made."""
    internal_error_message = 'API error occurred. Access to data failed.'
    user_error_message = 'Sorry, you have reached 10 calls per second limit.'
    status = 'API Error - 10 calls limit reached.'


class DatabaseException(BaseAPPException):  # Level 2 exception
    """Database general exception"""
    internal_error_message = 'Database error occurred.'
    user_error_message = 'An unexpected error with database occurred.'
    status = 'Database Error.'
