from django.contrib import admin
from .models import order,favorite
# Register your models here.

@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["house","startDate","endDate","client"]

@admin.register(favorite)
class favoriteAdmin(admin.ModelAdmin):
    list_display = ["house","client"]

# admin.site.register(order)