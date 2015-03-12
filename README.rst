dj-sso-client
=============
``dj-sso-client`` is the a Django application works as SSO client side of ``dj-sso-server`` (https://github.com/feifangit/dj-sso-server)


Installation
-------------
``pip install dj-sso-client``



Add to your project
------------------------
- Modify following settings in ``settings.py`` of your project

	- ``AUTHENTICATION_BACKENDS``, add ``djssoclient.authbackend.SSOAuthBackend`` as the backends
	- ``AUTH_USER_MODEL``, set ``djssoclient.SSOUser`` as user model

.. code-block:: python

	AUTHENTICATION_BACKENDS = ('djssoclient.authbackend.SSOAuthBackend',)
	AUTH_USER_MODEL = 'djssoclient.SSOUser'

- Add following ``dj-sso-client`` settings base on your demand

	- ``SSO_API_AUTH_SETTING``: set API key, SEC key and remote SSO provider URL. This setting is used by underneath ``dj-api-auth`` module to proejct API accessing.

		.. code-block:: python

			SSO_API_AUTH_SETTING = {
			    "apikey": "f4a05287",
			    "seckey": "6a4eeaea54d54f51af703e79c6096d51",
			    "url": "https://dj-sso-sample.herokuapp.com",
			}

	- ``SSO_REMOTE_URL_PREFIX`` (optional): SSO path in remote SSO provider. default ``/sso/``

	- ``SSO_USER_STORAGE``(optional):  SSOUser storage solution, there are 2 storage backends in ``dj-sso-client`` already. default: SSOUserDBStorage

		- ``djssoclient.userstorage.SSOUserDBStorage``: store user data in database
		- ``djssoclient.userstorage.SSOUserCacheStorage``: store user data in cache. You will get better performance.

	- ``SSO_SETTING_CACHE`` (optional): if you selected ``SSOUserCacheStorage`` as your user storage backend, and you have more than one cache in ``settings.py``, you can pick up the cache name here. default: ``default``


Attention: ``SSOUserCacheStorage``
---------------------------------------
The default ``django.core.cache.backends.locmem.LocMemCache`` stores data per process. In multi-process production environment (gunicorn on multi-core server), it may cause problem while using ``SSOUserCacheStorage`` as your user storage engine. 

Please use dedicate cache system (Memcached or Redis) as cache backend to avoid this problem.


SSOUser
--------
``SSOUser`` is the user model to store user data. It can be used as database model class if you selected ``SSOUserDBStorage`` to be your user storage engine.

.. code-block:: python
	
	class SSOUser(AbstractBaseUser):
	    username = models.CharField(unique=True, max_length=50)
	    extras = models.TextField(default="{}")
	    ...

**extra user attributes** : attributes not exists in the ``SSOUser`` class. (attributes except ``username``, ``password``, ``last_login`` etc.) 

All extra user attributes can be access  by ``getattr`` method or ``.`` operator. And they are stored in class member ``extras`` in JSON format.


Get your hands dirty
---------------------
We already have a SSO provider (``dj-sso-server``) application running on Heroku: http://dj-sso-sample.herokuapp.com/ . Run the example application in folder ``example/ssoclient/`` locally.

The API key using in the example application is binding with ``localhost:8000``, so make sure you're accessing local application by ``localhost:8000`` rather than the ``127.0.0.1:8000``. 

**fresh login**

1. make sure you're not logged in on http://dj-sso-sample.herokuapp.com/, you should see ``please log in with ...``
2. click *sso login* on local application, you will be redirected to http://dj-sso-sample.herokuapp.com/sso/....
3. you will see user information after be redirected to local application.
4. on http://dj-sso-sample.herokuapp.com/ , your status is still not logged-in

**login with existing logged account**

1. log in with user name ``user1`` and password ``123`` on http://dj-sso-sample.herokuapp.com/ 
2. click  *sso login* on local application, you will be redirected to http://dj-sso-sample.herokuapp.com/sso/...., but you will see a different login page with fresh login. 
3. select ``continue with current user? user1``
4. you will be logged in as ``user1`` at local application

**switch account**

1. if you select ``switch account`` and login with ``user2``/``456`` from step 3 in previous sample
2. you will be logged in as ``user2`` at local application
3. your login status on http://dj-sso-sample.herokuapp.com/ will **NOT** be changed (still logged in as ``user1``)



TODO
-----
- example: work as an extra auth method

