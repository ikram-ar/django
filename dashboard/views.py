from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import ProtectedError, RestrictedError
from dashboard.forms import EstablishmentForm, NormalUserForm, UserGroupForm
from dashboard.models import Establishment, NormalUser, Command
from django.contrib.auth.models import Group
from django.db.models import Count

# Vue de la page d'accueil
@login_required
def home(request):
    user_count = NormalUser.objects.count() 
    
    # Récupérer les données des commandes et les agréger par date et statut
    commands_data = Command.objects.values('created_at', 'status') \
        .annotate(count=Count('id')) \
        .order_by('created_at')

    # Préparer les données pour le graphique
    dates = []
    status_counts = {
        'en cours': {},
        'annulé': {},
        'livré': {},
    }

    # Organiser les données par date et statut
    for data in commands_data:
        date_str = data['created_at'].strftime('%Y-%m-%d')  # Formater la date en chaîne
        if date_str not in dates:
            dates.append(date_str)

        status_counts[data['status']][date_str] = data['count']

    # Préparer les listes finales pour chaque statut
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


# --- Gestion des utilisateurs ---
# Vue de la liste des utilisateurs
@login_required
def utilisateur_view(request):
    users = NormalUser.objects.all()  
    context = {
        'current_section': 'utilisateur', 
        'users': users,  
    }
    return render(request, 'user/utilisateur.html', context)

# Ajouter un utilisateur
@login_required
def add_user(request):
    if request.method == 'POST':
        form = NormalUserForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Utilisateur ajouté avec succès !")
            return redirect('dashboard:utilisateur')  
        else:
            messages.error(request, "Erreur lors de l'ajout de l'utilisateur.")
    else:
        form = NormalUserForm()
    
    return render(request, 'user/add_user.html', {'form': form, 'current_section': 'utilisateur'})

# Modifier un utilisateur
def edit_user(request, user_id):
    user = get_object_or_404(NormalUser, pk=user_id)

    if request.method == 'POST':
        form = NormalUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  
            messages.success(request, "Utilisateur mis à jour avec succès !")
            return redirect('dashboard:utilisateur')
        else:
            messages.error(request, "Erreur lors de la mise à jour de l'utilisateur.")
    else:
        form = NormalUserForm(instance=user)

    return render(request, 'user/edit_user.html', {'form': form, 'user': user, 'current_section': 'utilisateur'})

# Supprimer un utilisateur
def delete_user(request, user_id):
    user = get_object_or_404(NormalUser, id=user_id)
    try:
        user.delete()  
    except RestrictedError as e:
        messages.error(request, "Impossible de supprimer l'utilisateur car il est associé à un ou plusieurs établissements.")
    return redirect('dashboard:utilisateur')


# --- Gestion des établissements ---
# Vue des établissements
@login_required
def etablissement_view(request):
    etablissements = Establishment.objects.all()  
    context = {
        'current_section': 'etablissement',  
        'etablissements': etablissements, 
    }
    return render(request, 'etablissement/etablissement.html', context)

# Ajouter un établissement
@login_required
def add_etablissement(request):
    if request.method == 'POST':
        form = EstablishmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, "Établissement ajouté avec succès !")
            return redirect('dashboard:etablissement')
        else:
            messages.error(request, "Erreur lors de l'ajout de l'établissement.")
    else:
        form = EstablishmentForm()
    return render(request, 'etablissement/add_etablissement.html', {'form': form, 'current_section': 'etablissement'})

# Modifier un établissement
def edit_etablissement(request, etablissement_id):
    etablissement = get_object_or_404(Establishment, pk=etablissement_id)
    if request.method == 'POST':
        form = EstablishmentForm(request.POST, instance=etablissement)
        if form.is_valid():
            form.save()  
            messages.success(request, "Établissement mis à jour avec succès !")
            return redirect('dashboard:etablissement')
        else:
            messages.error(request, "Erreur lors de la mise à jour de l'établissement.")
    else:
        form = EstablishmentForm(instance=etablissement)
    return render(request, 'etablissement/edit_etablissement.html', {'form': form, 'etablissement': etablissement, 'current_section': 'etablissement'})

# Supprimer un établissement
def delete_etablissement(request, etablissement_id):
    etablissement = get_object_or_404(Establishment, pk=etablissement_id)
    etablissement.delete()  
    messages.success(request, "Établissement supprimé avec succès !")
    return redirect('dashboard:etablissement')


# --- Gestion des groupes d'utilisateurs ---
# Vue des groupes d'utilisateurs
@login_required
def groupes_view(request):
    usergroups = Group.objects.all()  
    return render(request, 'usergroup/groupes.html', {'usergroups': usergroups, 'current_section': 'groupes'})

# Ajouter un groupe d'utilisateurs
@login_required
def usergroup_add(request):
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Groupe d'utilisateurs ajouté avec succès !")
            return redirect('dashboard:groupes')
        else:
            messages.error(request, "Erreur lors de l'ajout du groupe d'utilisateurs.")
    else:
        form = UserGroupForm()
    return render(request, 'usergroup/add_usergroup.html', {'form': form, 'current_section': 'groupes'})

# Modifier un groupe d'utilisateurs
@login_required
def usergroup_edit(request, pk):
    usergroup = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = UserGroupForm(request.POST, instance=usergroup)
        if form.is_valid():
            form.save()  
            messages.success(request, "Groupe d'utilisateurs mis à jour avec succès !")
            return redirect('dashboard:groupes')
        else:
            messages.error(request, "Erreur lors de la mise à jour du groupe d'utilisateurs.")
    else:
        form = UserGroupForm(instance=usergroup)
    return render(request, 'usergroup/edit_usergroup.html', {'form': form, 'usergroup': usergroup, 'current_section': 'groupes'})

# Supprimer un groupe d'utilisateurs
@login_required
def usergroup_delete(request, pk):
    usergroup = get_object_or_404(Group, pk=pk)
    usergroup.delete()  
    messages.success(request, "Groupe d'utilisateurs supprimé avec succès !")
    return redirect('dashboard:groupes')

