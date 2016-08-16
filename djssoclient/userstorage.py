import cPickle
from . import SSO_SETTING_CACHE
from django.core.cache import caches
from django.db import IntegrityError
from .models import SSOUser


class SSOUserStorage(object):
    class Meta:
        abstract = True

    def save(self, userid, ssouser):
        raise NotImplementedError()

    def find(self, userid):
        raise NotImplementedError()

    def remove(self, userid):
        raise NotImplementedError()


class SSOUserCacheStorage(SSOUserStorage):
    def __init__(self):
        self.cache = caches(SSO_SETTING_CACHE)

    def _get_cached_id(self, userid):
        return "sso_user_%s" % userid

    def save(self, userid, ssouser):
        self.cache.set(self._get_cached_id(userid),
                       cPickle.dumps(ssouser), timeout=None)

    def find(self, userid):
        return cPickle.loads(self.cache.get(self._get_cached_id(userid)))

    def remove(self, userid):
        self.cache.delete(self._get_cached_id(userid))


class SSOUserDBStorage(SSOUserStorage):
    def save(self, userid, ssouser):
        try:
            ssouser.save()
        except IntegrityError:
            SSOUser.objects.filter(username=ssouser.username).delete()
            ssouser.save()

    def find(self, userid):
        try:
            return SSOUser.objects.get(pk=userid)
        except SSOUser.DoesNotExist:
            return None

    def remove(self, userid):
        pass
