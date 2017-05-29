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

    # /showcase/<seller_id>/checkin
    url(r'^(?P<seller_id>[0-9]+)/check_in/$', views.check_in, name='check_in'),

    # /showcase/<seller_id>/checkin
    url(r'^statistics/$', views.statistics, name='statistics'),

    # /showcase/item_new
    url(r'^item_new/$', views.item_new, name='item_new'),

    url(r'^item_edit/$', views.item_edit, name='item_edit'),

    # /showcase/item/<item_id>/
    # url(r'^$', views.index, name='index'),
]
