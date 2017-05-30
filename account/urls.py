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
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    url(r'^delete/$', views.delete_user, name='delete'),

    url(r'^delete/confirmation/$', views.confirm_deleted, name='confirm_deleted'),

    url(r'^edit/$', views.edit_user, name='edit_user'),

    url(r'^edit/client$', views.edit_client, name='edit_client'),

    url(r'^edit/peddler$', views.edit_peddler, name='edit_peddler'),

    url(r'^edit/established$', views.edit_established, name='edit_established'),

    # /account/register
    url(r'^register/$', views.register, name='register'),

    # /account/confirmation
    url(r'^confirmation/$', views.confirm_registration, name='confirm_registration'),

    # /account/register/client
    url(r'^register/client/$', views.register_client, name='register_client'),

    # /account/register/peddler
    url(r'^register/peddler/$', views.register_peddler, name='register_peddler'),

    # /account/register/established
    url(r'^register/established/$', views.register_established, name='register_established'),

    # /account/login
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    # /account/logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/account/login'}, name='logout'),

    # /password*
    url(r'^password_reset/$', auth_views.password_reset,
        {'template_name': 'account/templates/password_reset_form.html'},
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'account/templates/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'account/templates/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'account/templates/password_reset_complete.html'},
        name='password_reset_complete')
]
