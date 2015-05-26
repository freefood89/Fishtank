from flask import jsonify

class ApiException(Exception):

    def __init__(self, message, status_code, culprit=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.culprit = culprit

    def to_dict(self):
        error_dict = {}
        error_dict['culprit'] = self.culprit
        error_dict['message'] = self.message
        error_dict['code'] = self.status_code
        return error_dict
