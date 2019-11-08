import urllib

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from django.core.exceptions import PermissionDenied
from django.urls import reverse

from .apiclient import client
from . import REMOTE_REQUEST_TOKEN_URL, REMOTE_SSO_LOGIN_URL


def viewAuth(request):
    request_token = request.GET.get("request_token")
    auth_token = request.GET.get("auth_token")
    redirect_to = request.GET.get("redirect", settings.LOGIN_REDIRECT_URL)

    user = authenticate(request_token=request_token, auth_token=auth_token)
    if user is not None:
        auth_login(request, user)  # create session, write cookies
    else:
        raise PermissionDenied
    return HttpResponseRedirect(redirect_to)


def viewLogin(request):
    _, token_info = client.send_request(REMOTE_REQUEST_TOKEN_URL)
    request_token = token_info["request_token"]

    restserver = settings.SSO_API_AUTH_SETTING["url"]
    url_parts = list(urllib.parse.urlparse(restserver))
    query = {"api_key": settings.SSO_API_AUTH_SETTING["apikey"],
             "request_token": request_token,
             "next": request.build_absolute_uri(
                 reverse("djssoclient:ssoauth") + "?redirect=%s" % request.GET.get("next", settings.LOGIN_REDIRECT_URL))}
    if hasattr(settings, 'SSO_NO_CONFIRM'):
        query.update({'noconfirm': settings.SSO_NO_CONFIRM})
    url_parts[2] = REMOTE_SSO_LOGIN_URL
    url_parts[4] = urllib.parse.urlencode(query)
    ssoLoginURL = urllib.parse.urlunparse(url_parts)
    return HttpResponseRedirect(ssoLoginURL)
