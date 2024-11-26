from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import ProtectedError, RestrictedError
from dashboard.forms import EstablishmentForm, NormalUserForm
from dashboard.models import Establishment, NormalUser, UserGroup
from django.views.decorators.cache import never_cache


@login_required
def home(request):
    user_count = NormalUser.objects.count()
    
    # Fetch commands data and aggregate by date and status
    commands_data = Command.objects.values('created_at', 'status') \
        .annotate(count=Count('id')) \
        .order_by('created_at')

    # Prepare the data for the chart
    dates = []
    status_counts = {
        'en cours': {},
        'annulé': {},
        'livré': {},
    }

    for data in commands_data:
        date_str = data['created_at'].strftime('%Y-%m-%d')  # Format the date as string
        if date_str not in dates:
            dates.append(date_str)

        status_counts[data['status']][date_str] = data['count']

    # Prepare the final lists for each status
    en_cours = [status_counts['en cours'].get(date, 0) for date in dates]
    annule = [status_counts['annulé'].get(date, 0) for date in dates]
    livre = [status_counts['livré'].get(date, 0) for date in dates]

    context = {
        'dates': dates,
        'en_cours': en_cours,
        'annule': annule,
        'livre': livre,
        'current_section': 'dashboard',
        'user_count': user_count,
    }

    
    return render(request, 'home.html', context)



@login_required
def utilisateur_view(request):
    users = NormalUser.objects.all()
    context = {
        'current_section': 'utilisateur',
        'users': users,  # Pass the actual 'users' queryset here
    }
    print(users)
    return render(request, 'user/utilisateur.html', context)




from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NormalUserForm, UserGroupForm  # Adjust this import according to your project structure
@login_required
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
    
    return render(request, 'user/add_user.html', {'form': form, 'current_section': 'utilisateur'})

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

    return render(request, 'user/edit_user.html', {'form': form, 'user': user, 'current_section': 'utilisateur'})

def delete_user(request, user_id):
    user = get_object_or_404(NormalUser, id=user_id)
    
    try:
        user.delete()
    except RestrictedError as e:
        # Affiche uniquement le message d'erreur spécifique
        messages.error(request, "Impossible de supprimer l'utilisateur car il est associé à un ou plusieurs établissements.")
    
    return redirect('dashboard:utilisateur')



# --- Établissement management views ---
@login_required
def etablissement_view(request):
    etablissements = Establishment.objects.all()
    context = {
        'current_section': 'etablissement',
        'etablissements': etablissements,
    }
    return render(request, 'etablissement/etablissement.html', context)

@login_required
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
    return render(request, 'etablissement/add_etablissement.html', {'form': form, 'current_section': 'etablissement'})

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
    return render(request, 'etablissement/edit_etablissement.html', {'form': form, 'etablissement': etablissement ,'current_section': 'etablissement'})

def delete_etablissement(request, etablissement_id):
    etablissement = get_object_or_404(Establishment, pk=etablissement_id)
    etablissement.delete()
    messages.success(request, "Établissement deleted successfully!")
    return redirect('dashboard:etablissement')

#####
@login_required
def groupes_view(request):
    usergroups = UserGroup.objects.all()
    return render(request, 'usergroup/groupes.html', {'usergroups': usergroups, 'current_section': 'groupes',})

# Add UserGroup
@login_required
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
    return render(request, 'usergroup/add_usergroup.html', {'form': form, 'current_section': 'usergroup'})

# Edit UserGroup
@login_required
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
    return render(request, 'usergroup/edit_usergroup.html', {'form': form, 'usergroup': usergroup, 'current_section': 'usergroup'})

# Delete UserGroup
@login_required
def usergroup_delete(request, pk):
    usergroup = get_object_or_404(UserGroup, pk=pk)
    usergroup.delete()
    messages.success(request, "User Group deleted successfully!")
    return redirect('dashboard:groupes')



from django.shortcuts import render
from django.db.models import Count
from .models import Command


