from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(null=True)


class Peddler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(null=True)
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    social = models.BooleanField(default=False)


class Established(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(null=True)
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    social = models.BooleanField(default=False)
    start = models.TimeField()
    end = models.TimeField()


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)


class Dish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.FileField()
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.CharField(max_length=300)
    stock = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
