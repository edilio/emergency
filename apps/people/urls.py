from __future__ import unicode_literals

from django.conf.urls import patterns, url

from rest_framework import routers

from . import views

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'people', views.PersonViewSet)

urlpatterns = [

]

urlpatterns += router.urls


