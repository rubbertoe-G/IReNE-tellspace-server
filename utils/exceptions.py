"""
exceptions.py
====================================
Classes to standardize the exception raising.
"""

import datetime
from utils.logger import AppLogger


class TellSpaceError(Exception):
    """Base Audit Manager Error Class. When called, it will write error logs to the error_logs.log file."""

    error_type = 'TellSpace Error'

    def __init__(self, err=None, msg='Error', status=500, action=None):
        self.logger = AppLogger()
        self.msg = msg
        self.status = status
        if err:
            self.error_stack = [str(x).replace('"', "'") for x in err.args]
        else:
            self.error_stack = []
        self.error_stack.append(msg)
        self.err = err
        self.action = action
        self.status = status
        self.now = datetime.datetime.now()
        self.log()

    def log(self):
        log_string = '"error":"{}","error_type":"{}","log_action":"{}",' \
                     '"error_description":"{}","status":"{}", "time_stamp": "{}"'.format(
            str(self.err).replace('"', "'"),
            str(self.error_type).replace('"', "'"),
            str(self.action).replace('"', "'"),
            str(self.error_stack),
            str(self.status),
            str(self.now.strftime("%a, %d %b %Y %I:%M:%S %p"))
        )
        log_string = '{' + log_string + '},\n'

        self.logger.log_error(log_string)

    def __str__(self):
        return f'\nApplication is in DEBUG MODE:\nError Pretty Print:\n\tType:{self.error_type}; Msg:{self.msg}; Status:{self.status}; ' \
               f'ErrStackTrace:{self.error_stack}'


class TellSpaceApiError(TellSpaceError):
    """Audit Manager for any error"""
    error_type = 'TellSpace Api Error'


class TellSpaceAuthError(TellSpaceError):
    """Audit manager for authentication errors"""
    error_type = 'TellSpace Authentication Error'
