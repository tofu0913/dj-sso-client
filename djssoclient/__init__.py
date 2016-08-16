import os
from django.conf import settings
from .version import __version__, VERSION


def _load_setting(n, default):
    return getattr(settings, n) if hasattr(settings, n) else default

remote_sso_url_prefix = _load_setting("SSO_REMOTE_URL_PREFIX", "/sso/")
REMOTE_REQUEST_TOKEN_URL = os.path.join(remote_sso_url_prefix, "reqeusttoken/")
REMOTE_AUTH_TOKEN_URL = os.path.join(remote_sso_url_prefix, "authtoken/")
REMOTE_SSO_LOGIN_URL = os.path.join(remote_sso_url_prefix, "login/")


# user storage
SSO_USER_STORAGE = _load_setting("SSO_USER_STORAGE", "djssoclient.userstorage.SSOUserDBStorage")
SSO_SETTING_CACHE = _load_setting("SSO_SETTING_CACHE", "default")
