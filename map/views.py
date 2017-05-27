from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    chino = User.objects.get(username='chino')
    empanada = User.objects.get(username='empanada')
    lunchbox = User.objects.get(username='lunchbox')
    sushi = User.objects.get(username='sushi')
    pepe = User.objects.get(username='pepe')
    context = {'chino': chino, 'empanada': empanada, 'lunchbox': lunchbox, 'sushi': sushi, 'pepe':pepe}
    return render(request, 'index.html', context)
