import urllib
from django.utils.module_loading import import_string
from .models import SSOUser
from . import REMOTE_AUTH_TOKEN_URL, SSO_USER_STORAGE
from .apiclient import client


class SSOAuthBackend(object):
    def __init__(self):
        SSO_USER_STORAGE_CLZ = import_string(SSO_USER_STORAGE)
        self.storageengine = SSO_USER_STORAGE_CLZ()

    def authenticate(self, request, request_token=None, auth_token=None, **credentials):
        code, user_info = client.send_request(
            REMOTE_AUTH_TOKEN_URL + "?" + urllib.parse.urlencode({"request_token": request_token, "auth_token": auth_token}))
        user = user_info["user"]
        u = SSOUser(**user)
        self.storageengine.save(user["id"], u)
        return u

    def get_user(self, user_id):
        return self.storageengine.find(user_id)
