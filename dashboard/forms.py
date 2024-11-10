from django import forms
from .models import NormalUser, UserGroup
from .models import Establishment

class NormalUserForm(forms.ModelForm):
    class Meta:
        model = NormalUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'manager_name': forms.TextInput(attrs={'class': 'form-control'}),
            'foundation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'nif_cin': forms.TextInput(attrs={'class': 'form-control'}),
            'rc_license': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'establishment_type': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'users': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }