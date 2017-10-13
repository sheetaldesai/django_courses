from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^add/$', views.add, name="add"),
    url(r'^(?P<id>[0-9]+)/remove/$', views.remove, name='remove'),
    url(r'^(?P<id>[0-9]+)/removeConfirm/$', views.removeConfirm, name="removeConfirm"),
    # url(r'^addEdit/(?P<userId>[0-9]+)/$', views.addEdit, name="addEdit"),
    # url(r'^(?P<userId>[0-9]+)/edit/$', views.edit, name='edit'),
    # url(r'^/(?P<userId>[0-9]+)/delete/$', views.delete, name='delete')
]