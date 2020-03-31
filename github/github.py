import json
import requests
from .issues import issues
from .pullreqs import pullreqs
from .events import events
from .orgs import orgs
from .users import users
from .repos import repos


class Github:
    apiurl = 'https://api.github.com'
    suffix = "access_token="

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.issues = issues.Issues(self)
        self.orgs = orgs.Orgs(self)
        self.pullreqs = pullreqs.PullReq(self)
        self.repos = repos.Repos(self)
        self.users = users.Users(self)
        self.events = events.Events(self)

    def execute(self, httpVerb, path, data=None):
        verb = str.upper(httpVerb)
        url = self.__buildurl(path)
        if verb == 'HEAD':
            return self.head(url)
        elif verb == 'GET':
            return self.get(url)
        elif verb == 'POST':
            return self.post(url, data)
        elif verb == 'PATCH':
            return self.patch(url, data)
        elif verb == 'PUT':
            return self.put(url, data)
        elif verb == 'DELETE':
            return self.delete(url)
        else:
            raise Exception(
                'Invalid httpVerb. Use: head, get, post, patch, put, delete')

    def head(self, url):
        url = self.__buildurl(url)
        r = requests.head(url, auth=(self.username, self.password))
        return self.__buildResponse(r)

    def get(self, url):
        url = self.__buildurl(url)
        # r = requests.get(url, auth=(self.username, self.password))
        params = {
            "access_token": "78854faee2ae023107ee2699c35d2229d194a36d"
        }
        r = requests.get(url, params=params)
        print(r.url)
        return self.__buildResponse(r)

    def post(self, url, data=None):
        url = self.__buildurl(url)
        r = requests.post(url, data=data,
                          auth=(self.username, self.password))
        return self.__buildResponse(r)

    def patch(self, url, data):
        url = self.__buildurl(url)
        r = requests.patch(url, data=data,
                           auth=(self.username, self.password))
        return self.__buildResponse(r)

    def put(self, url, data=None):
        url = self.__buildurl(url)
        r = requests.put(url, data=data,
                         auth=(self.username, self.password))
        return self.__buildResponse(r)

    def delete(self, url, data=None):
        url = self.__buildurl(url)
        r = requests.post(url, data=data,
                          auth=(self.username, self.password))
        return self.__buildResponse(r)

    def __removeEmptyParams(self, params):
        return dict((k, v) for k, v in params.iteritems() if v is not None)

    def __buildurl(self, path):
        print(Github.apiurl + (path if (path[0] is '/') else ('/%s' % path)))
        return Github.apiurl + (path if (path[0] is '/') else ('/%s' % path))

    def __buildResponse(self, response):
        headers = json.dumps(dict(response.headers))
        body = response.json()
        # return {
        #     "headers": json.dumps(dict(response.headers)),
        #     "body": response.json()
        # }
        return headers, body
