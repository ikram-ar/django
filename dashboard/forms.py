from django import forms
from .models import NormalUser, UserGroup, Establishment, Group

class NormalUserForm(forms.ModelForm):
    class Meta:
        model = NormalUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }

class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = [
            'owner', 'name', 'manager_name', 'foundation_date', 'address',
            'nif_cin', 'rc_license', 'phone_number', 'email', 'description',
            'image', 'establishment_type', 'latitude', 'longitude', 'is_verified',
            'is_available', 'is_open', 'is_managed'
        ]
        widgets = {
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter establishment name'}),
            'manager_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter manager name'}),
            'foundation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'nif_cin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter NIF/CIN'}),
            'rc_license': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter RC/license'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'establishment_type': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter longitude'}),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_open': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_managed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UserGroupForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = ['name', 'users']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter group name'}),
            'users': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

# Consolidated Group Form for creating and editing groups
class GroupeForm(forms.ModelForm):
    class Meta:
        model = Group  # Ensure this references the correct model for groups
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter group name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
        }
