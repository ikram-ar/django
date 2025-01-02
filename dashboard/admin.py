from django.contrib import admin
from .models import Command, NormalUser, Establishment
from django.contrib.auth.models import Group

# Register your models here.


@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'group')  # Include 'group' in the list display
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('group',)  # Add group to the filter

admin.site.unregister(Group)  # Unregister the built-in Group model if you want to manage groups through NormalUser
admin.site.register(Group) 

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'phone_number', 'email', 'is_verified', 'is_available', 'is_open', 'is_managed')





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