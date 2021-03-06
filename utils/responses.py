"""
responses.py
====================================
Classes to standardize the response methods.
"""

from flask import jsonify, make_response


class ApiResult(object):
    """API result response wrapper class"""

    def __init__(self, status=200, **kwargs):
        self.res = jsonify(**kwargs)
        self.status = status

    def to_response(self):
        return make_response(self.res, self.status)


class ApiException(object):
    """API exception response wrapper class"""
    def __init__(self, error_type='ApiError', message='Error', status=500):
        self.res = jsonify(error_type=error_type, message=message, status=status)
        self.status = status

    def to_response(self):
        return make_response(self.res, self.status)

