__author__ = 'Casey Dunham'
__version__ = "0.1.2"


import urllib
import urllib2
import json


PWNED_API_URL = "https://haveibeenpwned.com/api/breachedaccount/%s"


class InvalidEmail(Exception):
    pass


def check(email):
    req = urllib2.Request(PWNED_API_URL % urllib.quote(email))
    try:
        resp = urllib2.urlopen(req)
        return json.loads(resp.read())
    except urllib2.HTTPError, e:
        if e.code == 400:
            raise InvalidEmail("Email address does not appear to be a valid email")
        return []

