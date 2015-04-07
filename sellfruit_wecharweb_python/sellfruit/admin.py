#!/usr/bin/python
#encoding=utf-8


from django.contrib import admin
from models import *
# from forms import *

# Register your models here.

admin.site.register(Order)
admin.site.register(Fruit)
admin.site.register(Comment)
