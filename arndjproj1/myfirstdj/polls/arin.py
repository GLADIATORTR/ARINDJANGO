__author__ = 'Necati'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.arin, name='index'),
]