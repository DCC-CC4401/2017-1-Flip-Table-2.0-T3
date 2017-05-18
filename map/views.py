from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)
