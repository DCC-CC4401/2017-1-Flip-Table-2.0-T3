from django.shortcuts import render, redirect
from .forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm, AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login as django_login


# Create your views here.

def edit(request):
    context = {}
    return render(request, 'account_edit.html', context)


def new_item(request):
    context = {}
    return render(request, 'item_new.html', context)


def register(request):
    return render(request, 'register_base.html')


def register_client(request):
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            return redirect('map:index')
    else:
        form = ClientCreateForm()
    return render(request, 'register_client.html', {'form': form})


def register_peddler(request):
    if request.method == 'POST':
        form = PeddlerCreateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            return redirect('map:index')
    else:
        form = PeddlerCreateForm()
    return render(request, 'register_peddler.html', {'form': form})


def register_established(request):
    if request.method == 'POST':
        form = EstablishedCreateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            return redirect('map:index')
    else:
        form = EstablishedCreateForm()
    return render(request, 'register_established.html', {'form': form})
