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

    # /showcase/<seller_id>/create_dish
    url(r'^(?P<seller_id>[0-9]+)/create_dish/$', views.create_dish, name='create_dish'),

    # /showcase/<seller_id>/update_dish/<dish_id>
    url(r'^(?P<seller_id>[0-9]+)/update_dish/(?P<dish_id>[0-9]+)/$', views.update_dish, name='update_dish'),

    # /showcase/<seller_id>/update_dish/<dish_id>/delete
    url(r'^(?P<seller_id>[0-9]+)/delete_dish/(?P<dish_id>[0-9]+)$', views.delete_dish, name='delete_dish'),

    # /showcase/<seller_id>/checkin
    url(r'^statistics/$', views.statistics, name='statistics'),

    url(r'^item_edit/$', views.item_edit, name='item_edit'),

    # /showcase/item/<item_id>/
    # url(r'^$', views.index, name='index'),
]
