from django import http

from json_utils import utils

class JSONResponse(http.HttpResponse):
    def __init__(self, content, content_type='application/json'):
        # Considered adding some CSRF protection. Decided against it in favour
        # of the Django middleware and other more generic solutions.
        content = utils.to_json(content)
        super(JSONResponse, self).__init__(content,
                                           content_type=content_type)
