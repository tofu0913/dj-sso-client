import copy
import pickle

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, update_last_login
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.auth import get_backends


def default_dumpped_dict():
    return pickle.dumps({})

class SSOUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    extras = models.TextField(default=default_dumpped_dict)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __init__(self, *args, **kwargs):
        fieldsOfModel = [x.name for x in self._meta.fields]  # fields can be saved in database

        _kwargs = copy.deepcopy(kwargs)
        extrainfo = {}
        for fn, fv in filter(lambda item: item[0] not in fieldsOfModel, kwargs.items()):
            _kwargs.pop(fn, None)  # only db fields in _kwargs
            extrainfo[fn] = fv
        _kwargs["extras"] = pickle.dumps(extrainfo)
        return super(SSOUser, self).__init__(*args, **_kwargs)


    def __getattribute__(self, name):
        val = None
        try:  # read from regular field
            val = super(SSOUser, self).__getattribute__(name)
        except AttributeError as e:  # try to read from extra field
            if name.startswith("__"):  # avoid affecting object stuff
                raise e

            try:
                val = pickle.loads(str(self.extras)).get(name)
            except Exception as oe:
                pass
        return val

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
        
    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

@receiver(user_logged_out, sender=SSOUser)
def notify_backend(request, user, *args, **kwargs):
    from .authbackend import SSOAuthBackend
    for b in get_backends():
        if isinstance(b, SSOAuthBackend):
            b.storageengine.remove(user.id)

user_logged_in.disconnect(update_last_login)
