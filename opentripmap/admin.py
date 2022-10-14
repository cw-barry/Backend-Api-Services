from django.contrib import admin
from .models import Location, Places
# Register your models here.

admin.site.register((Location,Places))
