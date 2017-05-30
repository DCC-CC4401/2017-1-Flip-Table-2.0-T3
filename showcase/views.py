from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Transaction

import datetime

from showcase.forms import DishForm

from account.models import Client, Peddler, Established
from showcase.admin import Dish


# Create your views here.

def index(request):
    context = {}
    return render(request, 'showcase.html', context)


def item_new(request):
    context = {}
    return render(request, 'create_dish.html', context)


def item_edit(request):
    context = {}
    return render(request, 'item_edit.html', context)


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
            seller = User.objects.get(id=seller_id)
            transaction = Transaction(user=seller, dish=dish, price=dish.price, quantity=dish.sold)
            transaction.save()
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


def check_in(request, seller_id):
    seller = get_object_or_404(User, id=seller_id)
    seller_profile = get_object_or_404(Peddler, user=seller)
    if seller_profile.available:
        seller_profile.available = False
    else:
        seller_profile.available = True
    seller_profile.save()
    return HttpResponse(status=204)


def create_dish(request, seller_id):
    form = DishForm(request.POST or None, request.FILES or None)
    user = get_object_or_404(User, id=seller_id)
    if form.is_valid():
        dishes = user.dish_set.all()
        for dish in dishes:
            if dish.name == form.cleaned_data['name']:
                context = {
                    'form': form,
                    'error_message': 'Ya tienes un plato con este nombre',
                }
                return render(request, 'create_dish.html', context)
        dish = form.save(commit=False)
        dish.icon = "default/" + dict(form.fields['choices'].choices)[form.cleaned_data['choices']]
        dish.user = user
        dish.image = request.FILES['image']
        dish.save()
        return redirect('showcase:showcase', seller_id)
    context = {
        'form': form,
    }
    return render(request, 'create_dish.html', context)


def update_dish(request, seller_id, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        form = DishForm(data=request.POST, files=request.FILES, instance=dish)
        if form.is_valid():
            dish.icon = "default/" + dict(form.fields['choices'].choices)[form.cleaned_data['choices']]
            dish.image = request.FILES['image']
            form.save()
            return redirect('showcase:showcase', seller_id)
    else:
        form = DishForm(instance=dish)
    return render(request, 'update_dish.html', {'form': form, 'seller_id': seller_id, 'dish_id': dish_id})


def delete_dish(request, seller_id, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.delete()
    return redirect('showcase:showcase', seller_id)


def statistics(request):
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
              'Noviembre', 'Diciembre']
    earnings = {}
    for i, month in enumerate(months):
        sum = 0
        for item in Transaction.objects.all():
            if item.date.month == i + 1 and request.user.username == item.user.username:
                sum += item.price * item.quantity
        earnings[month] = sum
    return render(request, 'statistics.html', {'months': months, 'earnings': earnings})
