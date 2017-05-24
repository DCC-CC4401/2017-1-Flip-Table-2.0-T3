"""flipTable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'showcase'

urlpatterns = [

    # /showcase/
    url(r'^$', views.index, name='index'),


    # /showcase/<seller_id>/
    url(r'^(?P<seller_id>[0-9]+)/$', views.ShowcaseView.as_view(), name='showcase'),


    # /showcase/item_new
    url(r'^item_new/$', views.item_new, name='item_new'),

    # /showcase/item/<item_id>/
    # url(r'^$', views.index, name='index'),
]
