from django.contrib import admin

from .models import *

admin.site.register((Maincateory,Subcateory,Brand,Product,checkout,contact))

