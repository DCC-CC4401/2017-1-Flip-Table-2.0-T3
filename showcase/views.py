from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User

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
    user = User.objects.get(id=seller_id)
    try:
        seller = Peddler.objects.get(user=user)
    except:
        seller = get_object_or_404(Established,user=user)
    isPeddler = seller.__class__ == Peddler
    img = seller.image
    dishes = user.dish_set.all()
    context = {'dishes': dishes, 'user': user,'isPeddler': isPeddler,'seller': seller,'image': img}
    return render(request, 'showcase.html', context)
