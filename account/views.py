from django.shortcuts import render, redirect
from .forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm, ClientUpdateForm
from .models import Peddler, Established


# Create your views here.

def edit(request):
    if request.user.__class__ == Peddler:
        return update_peddler(request)
    elif request.user.__class__ == Established:
        return update_established(request)
    else:
        return update_client(request)

def update_client(request):
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            return redirect('index.html')
        else:
            print("NOOOOOOOOOOOOOOOOOOOOO")
            return redirect('caca.html')
    else:
        form = ClientCreateForm()
    return render(request, 'account_edit.html', {'form': form})

def update_peddler(request):
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            return redirect('account_edit.html')
    else:
        form = ClientCreateForm()
    return render(request, 'account_edit.html', {'form': form})

def update_established(request):
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            return redirect('account_edit.html')
    else:
        form = ClientCreateForm()
    return render(request, 'account_edit.html', {'form': form})


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
