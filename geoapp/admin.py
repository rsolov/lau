# Register your models here.
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Marker


@admin.register(Marker)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('type', 'location')
