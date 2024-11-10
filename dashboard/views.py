from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from dashboard.forms import EstablishmentForm
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