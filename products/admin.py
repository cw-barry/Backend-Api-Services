from django.contrib import admin
from .models import Category, Products, Images
# Register your models here.
admin.site.register((Category, Products, Images))