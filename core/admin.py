from django.contrib import admin
from core.models import Booking, Item, Slot


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available']
    list_editable = ['price', 'is_available']


@admin.register(Slot)
class Slot(admin.ModelAdmin):
    list_display = ['start_time', 'end_time', 'available', 'is_active']
    list_editable = ['available', 'is_active']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'slot', 'item', 'status', 'created_at']
    list_editable = ['status']