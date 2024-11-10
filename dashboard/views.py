from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    context = {
        'current_section': 'utilisateur',
    }
    return render(request, 'utilisateur.html', context)

def groupes_view(request):
    context = {
        'current_section': 'groupes',
    }
    return render(request, 'groupe.html', context)