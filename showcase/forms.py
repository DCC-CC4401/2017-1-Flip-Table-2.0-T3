from django import forms
from .models import Dish
from django.contrib.admin import widgets


class DishCreateForm(forms.ModelForm):

        class Meta:
            model = Dish
            fields = ('dish_name', 'value', 'stock', 'tags', 'description', 'icon', 'image')

