from django import forms
from django.contrib.auth.models import Group, Permission
from .models import NormalUser, Establishment

# Constants for permission translations
PERMISSION_TRANSLATIONS = {
    'admin | logentry | Can add log entry': 'Peut ajouter une entrée de journal',
    'admin | logentry | Can change log entry': 'Peut modifier une entrée de journal',
    'admin | logentry | Can delete log entry': 'Peut supprimer une entrée de journal',
    'admin | logentry | Can view log entry': 'Peut voir une entrée de journal',
    'auth | group | Can add group': 'Peut ajouter un groupe',
    'auth | group | Can change group': 'Peut modifier un groupe',
    'auth | group | Can delete group': 'Peut supprimer un groupe',
    'auth | group | Can view group': 'Peut voir un groupe',
    'auth | permission | Can add permission': 'Peut ajouter une permission',
    'auth | permission | Can change permission': 'Peut modifier une permission',
    'auth | permission | Can delete permission': 'Peut supprimer une permission',
    'auth | permission | Can view permission': 'Peut voir une permission',
    'auth | user | Can add user': 'Peut ajouter un utilisateur',
    'auth | user | Can change user': 'Peut modifier un utilisateur',
    'auth | user | Can delete user': 'Peut supprimer un utilisateur',
    'auth | user | Can view user': 'Peut voir un utilisateur',
    'contenttypes | contenttype | Can add content type': 'Peut ajouter un type de contenu',
    'contenttypes | contenttype | Can change content type': 'Peut modifier un type de contenu',
    'contenttypes | contenttype | Can delete content type': 'Peut supprimer un type de contenu',
    'contenttypes | contenttype | Can view content type': 'Peut voir un type de contenu',
    'dashboard | command | Can add command': 'Peut ajouter une commande',
    'dashboard | command | Can change command': 'Peut modifier une commande',
    'dashboard | command | Can delete command': 'Peut supprimer une commande',
    'dashboard | command | Can view command': 'Peut voir une commande',
    'dashboard | establishment | Can add establishment': 'Peut ajouter un établissement',
    'dashboard | establishment | Can change establishment': 'Peut modifier un établissement',
    'dashboard | establishment | Can delete establishment': 'Peut supprimer un établissement',
    'dashboard | establishment | Can view establishment': 'Peut voir un établissement',
    'dashboard | normaluser | Can add normal user': 'Peut ajouter un utilisateur normal',
    'dashboard | normaluser | Can change normal user': 'Peut modifier un utilisateur normal',
    'dashboard | normaluser | Can delete normal user': 'Peut supprimer un utilisateur normal',
    'dashboard | normaluser | Can view normal user': 'Peut voir un utilisateur normal',
    'dashboard | revenue | Can add revenue': 'Peut ajouter des revenus',
    'dashboard | revenue | Can change revenue': 'Peut modifier des revenus',
    'dashboard | revenue | Can delete revenue': 'Peut supprimer des revenus',
    'dashboard | revenue | Can view revenue': 'Peut voir des revenus',
    'dashboard | usergroup | Can add user group': 'Peut ajouter un groupe d\'utilisateurs',
    'dashboard | usergroup | Can change user group': 'Peut modifier un groupe d\'utilisateurs',
    'dashboard | usergroup | Can delete user group': 'Peut supprimer un groupe d\'utilisateurs',
    'dashboard | usergroup | Can view user group': 'Peut voir un groupe d\'utilisateurs',
    'sessions | session | Can add session': 'Peut ajouter une session',
    'sessions | session | Can change session': 'Peut modifier une session',
    'sessions | session | Can delete session': 'Peut supprimer une session',
    'sessions | session | Can view session': 'Peut voir une session'
}

class NormalUserForm(forms.ModelForm):
    """Formulaire pour la gestion des utilisateurs normaux"""
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = NormalUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'group']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse email',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'group': 'Groupe',
        }

class EstablishmentForm(forms.ModelForm):
    """Formulaire pour la gestion des établissements"""
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
    """Formulaire pour la gestion des groupes d'utilisateurs"""
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Permissions"
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nom du groupe',
        }

    def __init__(self, *args, **kwargs):
        """Initialisation avec traduction des permissions"""
        super().__init__(*args, **kwargs)
        permissions_field = self.fields['permissions']
        translated_choices = [
            (perm.id, PERMISSION_TRANSLATIONS.get(
                f"{perm.content_type.app_label} | {perm.content_type.model} | {perm.name}",
                f"{perm.content_type.app_label} | {perm.content_type.model} | {perm.name}")
            ) for perm in permissions_field.queryset
        ]
        permissions_field.choices = translated_choices
