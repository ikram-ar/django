from django.contrib import admin
from .models import NormalUser, Establishment, Revenue, UserGroup
# Register your models here.


@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active')

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'phone_number', 'email', 'is_verified', 'is_available', 'is_open', 'is_managed')

@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('phone',)

@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('users',)
