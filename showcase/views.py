from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.http import JsonResponse

from account.models import Client, Peddler, Established


# Create your views here.

def index(request):
    context = {}
    return render(request, 'showcase.html', context)


def item_new(request):
    context = {}
    return render(request, 'item_new.html', context)


# class ShowcaseView(generic.ListView):
#     template_name = 'showcase.html'
#     context_object_name = 'dishes'  # <!-- default name: object_list -->
#
#     def get_queryset(self):
#         user = User.objects.get(id=self.kwargs['seller_id'])
#         return user.dish_set.all()


def showcase(request, seller_id):
    seller = User.objects.get(id=seller_id)
    try:
        seller_profile = Peddler.objects.get(user=seller)
    except:
        seller_profile = get_object_or_404(Established, user=seller)
    isPeddler = seller_profile.__class__ == Peddler

    isClient = False

    current_user = request.user
    print(current_user)
    if current_user.is_authenticated() and Client.objects.filter(user=current_user).exists():
        isClient = True

    isFavorite = False
    if not seller_profile.client_set.all().filter(id=current_user.id).first() is None:
        isFavorite = True

    favorite = 0

    if isPeddler:
        for client in Client.objects.all():
            if client.f_peddler.filter(id=seller_profile.id).exists():
                favorite += 1
    else:
        for client in Client.objects.all():
            if client.f_established.filter(id=seller_profile.id).exists():
                favorite += 1

    img = seller_profile.image
    dishes = seller.dish_set.all()
    context = {'dishes': dishes, 'seller': seller, 'isPeddler': isPeddler, 'seller_profile': seller_profile,
               'image': img,
               'isClient': isClient, 'isFavorite': isFavorite, 'favorite': favorite}

    return render(request, 'showcase.html', context)


def favorite_seller(request, seller_id):
    user = get_object_or_404(User, id=seller_id)
    client = get_object_or_404(Client, user=request.user)
    if Peddler.objects.filter(user=user).exists():
        seller = Peddler.objects.get(user=user)
        if client.f_peddler.filter(id=seller.id).exists():
            client.f_peddler.remove(seller)
        else:
            client.f_peddler.add(seller)
    elif Established.objects.filter(user=user).exists():
        seller = Established.objects.get(user=user)
        if client.f_established.filter(id=seller.id).exists():
            client.f_established.remove(seller)
        else:
            client.f_established.add(seller)
    client.save()
    return HttpResponse(status=204)
