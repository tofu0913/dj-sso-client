from django.urls import path

from .views import viewAuth

urlpatterns = [
    path(r'^auth/$', viewAuth, name="ssoauth"),

]
