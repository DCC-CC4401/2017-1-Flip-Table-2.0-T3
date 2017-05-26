# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 03:02
from __future__ import unicode_literals

from django.contrib.auth.models import User
from showcase.models import Dish, Tag

from django.db import migrations

def load_dish(apps, schema_editor):

    chino = User.objects.get(username='chino')
    empanada = User.objects.get(username='empanada')
    lunchbox = User.objects.get(username='lunchbox')
    sushi = User.objects.get(username='sushi')
    pepe = User.objects.get(username='pepe')

    dish1 = Dish(user=chino,name='carne mongoliana',image="static/img/rice.png", description='La carne mongoliana más rica que hayan probado',stock=20,price=2990)
    dish1.save()

    dish2 = Dish(user=chino,name='pollo mongoliano',image='static/img/rice.png',description='El pollo mongoliano mas ricoque hayan probado',stock=10,price=1990)
    dish2.save()

    dish3 = Dish(user=empanada,name='empanada de pino',image='static/img/rice.png',description='Empanada cacera con pino de carne mechada',stock=15,price=1000)
    dish3.save()

    dish4 = Dish(user=empanada,name='empanada de queso',image='static/img/rice.png',description='Empanada hecha con queso de campo',stock=5,price=1000)
    dish4.save()

    dish5 = Dish(user=lunchbox,name='arroz con pollo',image='static/img/rice.png',description='El mejor lunchbox que has omido',stock=8,price=2500)
    dish5.save()

    dish6 = Dish(user=sushi,name='sushi tempura',image='static/img/rice.png',description='Sushi relleno de pollo, queso crema y ciboulette',stock=12,price=1200)
    dish6.save()

    dish7 = Dish(user=pepe,name='lasagna',image='static/img/rice.png',description='Lasagna cacera con pino de lomo liso y pasas carozzi', stock=3,price=2300)
    dish7.save()

def delete_dishes(apps, schema_editor):

    chino = User.objects.get(username='chino')
    empanada = User.objects.get(username='empanada')
    lunchbox = User.objects.get(username='lunchbox')
    sushi = User.objects.get(username='sushi')
    pepe = User.objects.get(username='pepe')

    Dish.objects.get(user=lunchbox ,name='arroz con pollo').delete()
    Dish.objects.get(user=chino ,name='carne mongoliana').delete()
    Dish.objects.get(user=chino ,name='pollo mongoliana').delete()
    Dish.objects.get(user=empanada ,name='empanada de queso').delete()
    Dish.objects.get(user=empanada ,name='empanada de pino').delete()
    Dish.objects.get(user=sushi ,name='sushi tempura').delete()
    Dish.objects.get(user=pepe ,name='lasagna').delete()

def load_tag(apps, schema_editor):
    tag1 = Tag(name='pastas')
    tag1.save()

    tag2 = Tag(name='postres')
    tag2.save()

    tag3 = Tag(name='pack')
    tag3.save()

    tag4 = Tag(name='vegetariano')
    tag4.save()

    tag5 = Tag(name='vegano')
    tag5.save()

    tag6 = Tag(name='bajo en calorias')
    tag6.save()

def delete_tags(apps, schema_editor):
    Tag.objects.get(name='pastas').delete()
    Tag.objects.get(name='postres').delete()
    Tag.objects.get(name='pack').delete()
    Tag.objects.get(name='vegetariano').delete()
    Tag.objects.get(name='vegano').delete()
    Tag.objects.get(name='bajo en calorias').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
        ('account', '0003_auto_20170526_0300'),
    ]

    operations = [
        migrations.RunPython(load_dish,delete_dishes),
        migrations.RunPython(load_tag,delete_tags),
    ]
