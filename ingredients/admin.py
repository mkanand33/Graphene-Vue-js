# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Product, Family, Location,Category, Ingredient,Link

# Register your models here.

admin.site.register(Product)
admin.site.register(Family)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Link)