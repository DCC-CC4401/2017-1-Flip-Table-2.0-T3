# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 00:09
from __future__ import unicode_literals
from django.contrib.auth.models import User
from account.models import Client, Peddler, Established

from django.db import migrations

def load_client(apps, schema_editor):
    # Client = apps.get_model("account", "Client")

    user1 = User(username='alumno1', first_name='Tibo', last_name='Swy', email='tsy@bla.com', password='12345678abcd')
    user1.save()
    client1 = Client(user=user1)
    client1.save()

    user2 = User(username='alumno2', first_name='pepe', last_name='pepe2', email='pepe@pepe.com',
                 password='12345678abcd')
    user2.save()
    client2 = Client(user=user2)
    client2.save()


def load_paddler(apps, schema_editor):
    # Peddler = apps.get_model("account", "Paddler")

    user3 = User(username='chino', first_name='diego', last_name='diego2', email='diego@diego.com',
                 password='12345678abcd')
    user3.save()
    peddler1 = Peddler(user=user3)
    peddler1.save()

    user4 = User(username='lunchbox', first_name='juan', last_name='juan2', email='juan@juan.com',
                 password='12345678abcd')
    user4.save()
    peddler2 = Peddler(user=user4)
    peddler2.save()

    user5 = User(username='sushi', first_name='lucas', last_name='lucas2', email='lucas@lucas.com',
                 password='12345678abcd')
    user5.save()
    peddler3 = Peddler(user=user5)
    peddler3.save()


def load_estabished(apps, schema_editor):
    # Established = apps.get_model("account", "Established")

    user6 = User(username='pepe', first_name='pedro', last_name='pedro2', email='pedro@pedro.com',
                 password='12345678abcd')
    user6.save()
    established1 = Established(user=user6, start='10:20', end='20:34')
    established1.save()

    user7 = User(username='empanada', first_name='carlos', last_name='carlos2', email='carlos@carlos.com',
                 password='12345678abcd')
    user7.save()
    established2 = Established(user=user7, start='10:20', end='20:34')
    established2.save()


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170524_1438'),
    ]

    operations = [
        migrations.RunPython(load_client),
        migrations.RunPython(load_paddler),
        migrations.RunPython(load_estabished),
    ]