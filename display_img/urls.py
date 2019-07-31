#coding: utf-8
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.display_img, name = 'display_img'),
]
