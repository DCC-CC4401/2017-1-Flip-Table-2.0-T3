from django.shortcuts import render


# Create your views here.

def edit(request):
    context = {}
    return render(request, 'account_edit.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def register(request):
    context = {}
    return render(request, 'register.html', context)

def new_item(request):
    context = {}
    return render(request, 'item_new.html', context)
