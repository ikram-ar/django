from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from dashboard.forms import EstablishmentForm, NormalUserForm
from dashboard.models import NormalUser

@login_required

def home(request):
    context = {
        'current_section': 'dashboard',
    }
    return render(request, 'home.html', context)

def etablissement_view(request):
    context = {
        'current_section': 'etablissement',
    }
    return render(request, 'etablissement.html', context)


def utilisateur_view(request):
    users = NormalUser.objects.all()
    context = {
        'current_section': 'utilisateur',
        'users': users,  # Pass the actual 'users' queryset here
    }
    print(users)
    return render(request, 'utilisateur.html', context)


def groupes_view(request):
    context = {
        'current_section': 'groupes',
    }
    return render(request, 'groupe.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NormalUserForm  # Adjust this import according to your project structure

def add_user(request):
    if request.method == 'POST':
        form = NormalUserForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            form.save()
            messages.success(request, "User added successfully!")
            return redirect('dashboard:utilisateur')  # Redirect to the utilisateur list page
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
