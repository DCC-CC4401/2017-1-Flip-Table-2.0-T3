from django import forms
from .models import Dish
from django.contrib.admin import widgets


class DishCreateForm(forms.ModelForm):
    CHOICES = (
        ('1', 'bread.png',),
        ('2', 'breakfast.png',),
        ('3', 'burger.png',),
        ('4', 'chicken.png',),
        ('5', 'chicken2.png',),
        ('6', 'chocolate.png',),
        ('7', 'coke.png',),
        ('8', 'cupcake.png',),
        ('9', 'donut.png',),
        ('10', 'jelly.png',),
        ('11', 'fish.png',),
        ('12', 'fries.png',),
        ('13', 'hot-dog.png',),
        ('14', 'icecream.png',),
        ('15', 'juice.png',),
        ('16', 'lettuce.png',),
        ('17', 'pizza.png',),
        ('18', 'spaguetti.png',),
        ('19', 'rice.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Dish
        fields = ['name', 'price', 'stock', 'description', 'image']


class DishUpdateForm(forms.ModelForm):
    CHOICES = (
        ('1', 'bread.png',),
        ('2', 'breakfast.png',),
        ('3', 'burger.png',),
        ('4', 'chicken.png',),
        ('5', 'chicken2.png',),
        ('6', 'chocolate.png',),
        ('7', 'coke.png',),
        ('8', 'cupcake.png',),
        ('9', 'donut.png',),
        ('10', 'jelly.png',),
        ('11', 'fish.png',),
        ('12', 'fries.png',),
        ('13', 'hot-dog.png',),
        ('14', 'icecream.png',),
        ('15', 'juice.png',),
        ('16', 'lettuce.png',),
        ('17', 'pizza.png',),
        ('18', 'spaguetti.png',),
        ('19', 'rice.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Dish
        fields = ['name', 'price', 'stock', 'description', 'image']