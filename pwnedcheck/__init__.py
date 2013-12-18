__author__ = 'Casey Dunham'
__version__ = "0.1.0"


import urllib
import urllib2
import json


PWNED_API_URL = "https://haveibeenpwned.com/api/breachedaccount/%s"


class InvalidEmail(Exception):
    pass


def check(email):
    req = urllib.Request(PWNED_API_URL % urllib.quote(email))
    try:
        resp = urllib.urlopen(req)
        return json.loads(resp.read())
    except urllib2.HTTPError, e:
        if e.code == 400:
            raise InvalidEmail("Email address does not appear to be a valid email")
        return []

