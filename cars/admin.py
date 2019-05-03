from django.contrib import admin
from . import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'car_id',
        'owner',
        'color',
        'year',
        'manufacturer',
        'is_active',
    )
    filter_fields = (
        'year',
        'color',
        'manufacturer',
        'is_active',
    )
    search_fields = (
        'car_id',
    )
