from django.contrib import admin
from .models import Command, NormalUser, Establishment, UserGroup

# Register your models here.


@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active')

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'phone_number', 'email', 'is_verified', 'is_available', 'is_open', 'is_managed')



@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('users',)

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'status', 'created_at')

    # Filters to apply in the admin interface
    list_filter = ('status', 'created_at')

    # Add search capability to the admin panel
    search_fields = ('name', 'status')

    # Default ordering by created_at (most recent first)
    ordering = ('-created_at',)



