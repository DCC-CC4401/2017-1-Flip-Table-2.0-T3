from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'showcase'

urlpatterns = [

    # /showcase/
    url(r'^$', views.index, name='index'),


    # /showcase/<seller_id>/
    url(r'^(?P<seller_id>[0-9]+)/$', views.showcase, name='showcase'),

    # /showcase/<seller_id>/favorite
    url(r'^(?P<seller_id>[0-9]+)/favorite/$', views.favorite_seller, name='favorite_seller'),


    # /showcase/item_new
    url(r'^item_new/$', views.item_new, name='item_new'),

    # /showcase/item/<item_id>/
    # url(r'^$', views.index, name='index'),
]
