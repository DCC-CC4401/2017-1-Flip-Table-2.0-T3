from django.shortcuts import render


# Create your views here.

def index(request):
    context = {}
    return render(request, 'showcase.html', context)

def item_new(request):
    context = {}
    return render(request, 'item_new.html', context)