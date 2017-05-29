from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse

import datetime

from .forms import DishCreateForm

from account.models import Client, Peddler, Established
from showcase.admin import Dish


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
    if request.method == 'POST':
        new_stock = int(request.POST.get("stock_count", ""))
        dish_id = request.POST.get("dish_id", "")
        dish = get_object_or_404(Dish, id=dish_id)
        old_stock = dish.stock
        if new_stock < old_stock:
            dish.sold = old_stock - new_stock
        dish.stock = new_stock
        dish.save()
        return HttpResponse(status=204)
    else:
        seller = User.objects.get(id=seller_id)
        now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-4))).time()
        is_available = False
        try:
            seller_profile = Established.objects.get(user=seller)
            start = seller_profile.start
            end = seller_profile.end
            if start < now and now < end:
                is_available = True
        except:
            seller_profile = get_object_or_404(Peddler, user=seller)

        isPeddler = seller_profile.__class__ == Peddler

        isClient = False

        isPeddlerInHisProfile = False

        current_user = request.user
        if current_user.is_authenticated() and Client.objects.filter(user=current_user).exists():
            isClient = True

        if current_user.is_authenticated() and Peddler.objects.filter(
                user=current_user).exists() and current_user == seller:
            isPeddlerInHisProfile = True

        isFavorite = False
        if not seller_profile.client_set.all().filter(id=current_user.id).first() is None:
            isFavorite = True

        favorite = 0

        if isPeddler:
            for client in Client.objects.all():
                if client.f_peddler.filter(id=seller_profile.id).exists():
                    favorite += 1

        img = seller_profile.image
        dishes = seller.dish_set.all()
        context = {'dishes': dishes, 'seller': seller, 'isPeddler': isPeddler, 'seller_profile': seller_profile,
                   'image': img,
                   'isClient': isClient, 'isFavorite': isFavorite, 'favorite': favorite,
                   'isAvailable': is_available, 'isPeddlerInHisProfile': isPeddlerInHisProfile}

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


def checkin(request, seller_id):
    seller = get_object_or_404(User, id=seller_id)
    seller_profile = get_object_or_404(Peddler, user=seller)
    if seller_profile.available:
        seller_profile.available = False
    else:
        seller_profile.available = True
    seller_profile.save()
    return HttpResponse(status=204)


# def peddler_set_not_available(request, seller_id):
#     seller = get_object_or_404(User, id=seller_id)
#     seller_profile = get_object_or_404(Peddler, user=seller)
#     seller_profile.available = False
#     seller_profile.save()
#     return HttpResponse(status=204)

def creatingDish(request):
    if request.method == 'POST':
        form = DishCreateForm(request.POST)
        # if form.is_valid():
        #    user, user_profile = form.save()
        #    user.save()
        #    messages.add_message(request, 25, "Te has registrado con éxito")
        #    return redirect('account:confirm_registration')
    else:
        form = DishCreateForm()

    next = request.POST.get('next', '/')
    return HttpResponse(next)
