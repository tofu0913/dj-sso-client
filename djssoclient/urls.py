from django.conf.urls import patterns, url

from .views import viewAuth

urlpatterns = patterns('', url(r'^auth/$', viewAuth, name="ssoauth"), )
