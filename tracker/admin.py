from django.contrib import admin
from .models import CustomUser, Location


class CustomUserAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.register(CustomUser, CustomUserAdmin)
admin.register(Location, LocationAdmin)
