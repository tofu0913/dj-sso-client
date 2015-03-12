from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = patterns('',
    url(r'^$', 'ssoclient.views.home', name='home'),

    # login
    url(r'^accounts/login/$', 'djssoclient.views.viewLogin'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}),

    # sso
    url(r'^myssoclient/', include('djssoclient.urls')),
)
