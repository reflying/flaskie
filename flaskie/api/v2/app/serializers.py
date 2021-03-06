from flask_restplus import fields
from math import ceil
from flaskie import v2_api


class Pagination(object):
    """Creates pagination"""
    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
                num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

user_register = v2_api.model('Register Model', {
    'name': fields.String(required=True, default='Paulla Mboya', description='User fullname'),
    'username': fields.String(required=True, default='paulla', description='Username'),
    'email': fields.String(required=True, default='paulla@gmail.com', description='The user\'s email address'),
    'password': fields.String(required=True, default='mermaid', description='The users secret password'),
})

modify_user = v2_api.model('Update Model', {
    'name': fields.String(required=True, default='Paulla Mboya', description='User fullname'),
    'username': fields.String(required=True, default='paulla', description='Username'),
    'email': fields.String(required=True, default='paulla@gmail.com', description='The user\'s email address'),
})


user_login = v2_api.model('Login Model', {
    'username': fields.String(required=True, default='asheuh', description='Your username'),
    'password': fields.String(required=True, default='mermaid', description='Your password'),
})

requests = v2_api.model('Request Model', {
    'requestname': fields.String(required=True, default='Internet', description='Request name'),
    'description': fields.String(required=True, default='Slow internet connection', description='request description')
})

request_status = v2_api.model('Request status model', {
    'status': fields.String(required=True, default='Approved', description='Request status')
})

pagination = v2_api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_users = v2_api.inherit('Page of users', pagination, {
    'data': fields.List(fields.Nested(user_register, description='Array of users'))
})
