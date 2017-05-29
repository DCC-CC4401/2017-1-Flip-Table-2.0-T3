from django import forms
from .models import Dish
from django.contrib.admin import widgets


class DishCreateForm(forms.ModelForm):

        class Meta:
            model = Dish
            fields = ('name', 'price', 'stock', 'tags', 'description', 'image')

