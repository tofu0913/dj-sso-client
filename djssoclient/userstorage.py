import cPickle
from . import SSO_SETTING_CACHE
from django.core.cache import get_cache
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
        self.cache = get_cache(SSO_SETTING_CACHE)

    def _get_cached_id(self, userid):
        return "sso_user_%s" % userid

    def save(self, userid, ssouser):
        self.cache.set(self._get_cached_id(userid),
                       cPickle.dumps(ssouser))

    def find(self, userid):
        return cPickle.loads(self.cache.get(self._get_cached_id(userid)))

    def remove(self, userid):
        self.cache.delete(self._get_cached_id(userid))


class SSOUserDBStorage(SSOUserStorage):
    def save(self, userid, ssouser):
        ssouser.save()

    def find(self, userid):
        return SSOUser.objects.get(pk=userid)

    def remove(self, userid):
        try:
            SSOUser.objects.get(pk=userid).delete()
        except:
            pass
