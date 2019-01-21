# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Family(models.Model):
    reference = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    description = models.TextField()

    unit = models.CharField(max_length=10)

    minQuantity = models.FloatField()

    def __str__(self):
        return self.title


class Location(models.Model):
    reference = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    sku = models.CharField(max_length=13)
    barcode = models.CharField(max_length=13)

    title = models.CharField(max_length=200)
    description = models.TextField()

    unitCost = models.FloatField()
    unit = models.CharField(max_length=10)

    quantity = models.FloatField()
    minQuantity = models.FloatField()

    family = models.ForeignKey('Family')
    location = models.ForeignKey('Location')

    def __str__(self):
        return self.title


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.url


class Name(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approval = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve(self):
        self.approval = True
        self.save()

    def unpublish(self):
        self.published_date = None
        self.save()

    def disapprove(self):
        self.approval = False
        self.save()

    def __str__(self):
        return self.title


class Signup(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Comment(models.Model):
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, blank=True, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)


class Reply(models.Model):
    reply = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)


class Rating(models.Model):
    rating = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, blank=True, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'blog',)


class Like(models.Model):
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'blog',)