from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import ProtectedError
from dashboard.forms import EstablishmentForm, NormalUserForm
from dashboard.models import Establishment, NormalUser, UserGroup

@login_required

def home(request):
    context = {
        'current_section': 'dashboard',
    }
    return render(request, 'home.html', context)




def utilisateur_view(request):
    users = NormalUser.objects.all()
    context = {
        'current_section': 'utilisateur',
        'users': users,  # Pass the actual 'users' queryset here
    }
    print(users)
    return render(request, 'utilisateur.html', context)




from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NormalUserForm, UserGroupForm  # Adjust this import according to your project structure

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
    
    return render(request, 'add_user.html', {'form': form, 'current_section': 'utilisateur'})

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

    return render(request, 'edit_user.html', {'form': form, 'user': user, 'current_section': 'utilisateur'})

def delete_user(request, user_id):
    user = get_object_or_404(NormalUser, id=user_id)
    
    try:
        user.delete()
        messages.success(request, 'User deleted successfully.')
    except ProtectedError:
        messages.error(request, 'Cannot delete this user because they are referenced by other records.')

    return redirect('dashboard:user_list')



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
        form = EstablishmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Établissement added successfully!")
            return redirect('dashboard:etablissement')
        else:
            messages.error(request, "Error adding the établissement.")
    else:
        form = EstablishmentForm()
    return render(request, 'add_etablissement.html', {'form': form, 'current_section': 'etablissement'})

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
    return render(request, 'edit_etablissement.html', {'form': form, 'etablissement': etablissement ,'current_section': 'etablissement'})

def delete_etablissement(request, etablissement_id):
    etablissement = get_object_or_404(Establishment, pk=etablissement_id)
    etablissement.delete()
    messages.success(request, "Établissement deleted successfully!")
    return redirect('dashboard:etablissement')

#####

def groupes_view(request):
    usergroups = UserGroup.objects.all()
    return render(request, 'groupes.html', {'usergroups': usergroups, 'current_section': 'groupes',})

# Add UserGroup
def usergroup_add(request):
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Group added successfully!")
            return redirect('dashboard:groupes')
        else:
            messages.error(request, "Error adding the User Group.")
    else:
        form = UserGroupForm()
    return render(request, 'add_usergroup.html', {'form': form, 'current_section': 'usergroup'})

# Edit UserGroup
def usergroup_edit(request, pk):
    usergroup = get_object_or_404(UserGroup, pk=pk)
    if request.method == 'POST':
        form = UserGroupForm(request.POST, instance=usergroup)
        if form.is_valid():
            form.save()
            messages.success(request, "User Group updated successfully!")
            return redirect('dashboard:groupes')
        else:
            messages.error(request, "Error updating the User Group.")
    else:
        form = UserGroupForm(instance=usergroup)
    return render(request, 'edit_usergroup.html', {'form': form, 'usergroup': usergroup, 'current_section': 'usergroup'})

# Delete UserGroup
def usergroup_delete(request, pk):
    usergroup = get_object_or_404(UserGroup, pk=pk)
    usergroup.delete()
    messages.success(request, "User Group deleted successfully!")
    return redirect('dashboard:groupes')