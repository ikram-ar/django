from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from dashboard.forms import EstablishmentForm, NormalUserForm, GroupeForm
from dashboard.models import NormalUser, Establishment, UserGroup

@login_required
def home(request):
    context = {
        'current_section': 'dashboard',
    }
    return render(request, 'home.html', context)

# --- Établissement management views ---
def etablissement_view(request):
    etablissements = Establishment.objects.all()
    context = {
        'current_section': 'etablissement',
        'etablissements': etablissements,
    }
    return render(request, 'etablissement.html', context)

def add_etablissement(request):
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Établissement added successfully!")
            return redirect('dashboard:etablissement')
        else:
            messages.error(request, "Error adding the établissement.")
    else:
        form = EstablishmentForm()
    return render(request, 'add_etablissement.html', {'form': form})

def edit_etablissement(request, etablissement_id):
    etablissement = get_object_or_404(Establishment, pk=etablissement_id)
    if request.method == 'POST':
        form = EstablishmentForm(request.POST, instance=etablissement)
        if form.is_valid():
            form.save()
            messages.success(request, "Établissement updated successfully!")
            return redirect('dashboard:etablissement')
        else:
            messages.error(request, "Error updating the établissement.")
    else:
        form = EstablishmentForm(instance=etablissement)
    return render(request, 'edit_etablissement.html', {'form': form, 'etablissement': etablissement})

def delete_etablissement(request, etablissement_id):
    etablissement = get_object_or_404(Establishment, pk=etablissement_id)
    etablissement.delete()
    messages.success(request, "Établissement deleted successfully!")
    return redirect('dashboard:etablissement')

# --- User management views ---
def utilisateur_view(request):
    users = NormalUser.objects.all()
    context = {
        'current_section': 'utilisateur',
        'users': users,
    }
    return render(request, 'utilisateur.html', context)

def add_user(request):
    if request.method == 'POST':
        form = NormalUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully!")
            return redirect('dashboard:utilisateur')
        else:
            messages.error(request, "Error adding the user.")
    else:
        form = NormalUserForm()
    return render(request, 'add_user.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(NormalUser, pk=user_id)
    if request.method == 'POST':
        form = NormalUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect('dashboard:utilisateur')
        else:
            messages.error(request, "Error updating the user.")
    else:
        form = NormalUserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(NormalUser, pk=user_id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('dashboard:utilisateur')

# --- Groupe management views ---
def groupes_view(request):
    groupes = UserGroup.objects.all()
    context = {
        'current_section': 'groupes',
        'groupes': groupes,
    }
    return render(request, 'groupe.html', context)


def add_groupe(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new group to the database
            return redirect('dashboard:groupes')  # Redirect to the group list page
    else:
        form = GroupForm()

    return render(request, 'dashboard/add_groupe.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GroupForm  # Assuming you have a form for group update
from .models import Group

def edit_groupe(request, groupe_id):
    group = get_object_or_404(Group, id=groupe_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)  # Pass the existing group to update
        if form.is_valid():
            form.save()  # Update the group in the database
            return redirect('dashboard:groupes')  # Redirect to the group list page
    else:
        form = GroupForm(instance=group)  # Populate the form with existing group data

    return render(request, 'dashboard/edit_groupe.html', {'form': form, 'group': group})

def delete_groupe(request, groupe_id):
    groupe = get_object_or_404(UserGroup, pk=groupe_id)
    groupe.delete()
    messages.success(request, "Groupe deleted successfully!")
    return redirect('dashboard:groupes')
