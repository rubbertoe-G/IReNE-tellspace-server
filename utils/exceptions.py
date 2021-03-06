"""
exceptions.py
====================================
Classes to standardize the exception raising.
"""

import datetime


class TellSpaceError(Exception):
    """Base Audit Manager Error Class"""

    error_type = 'TellSpaceError'

    def __init__(self, err=None, msg='Error', status=500, action=None):
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

        # TODO: implement buffer
        with open('error_logs.log', 'a+') as f:
            f.write(log_string)

    def __str__(self):
        return f'\nApplication is in DEBUG MODE:\nError Pretty Print:\n\tType:{self.error_type}; Msg:{self.msg}; Status:{self.status}; ' \
               f'ErrStackTrace:{self.error_stack}'


class TellSpaceApiError(TellSpaceError):
    """Audit Manager API error"""
    error_type = 'TellSpaceApiError'


class TellSpaceRequestValidationError(TellSpaceError):
    """Audit Manager API error"""
    error_type = 'TellSpaceRequestValidationError'


class TellSpaceAuthError(TellSpaceError):
    """Error manager for authentication errors"""
    error_type = 'TellSpaceAuthError'
