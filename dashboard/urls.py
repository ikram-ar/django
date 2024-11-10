from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
  path('home/', views.home, name='home'),
    path('etablissement/', views.etablissement_view, name='etablissement'),

    path('utilisateur/', views.utilisateur_view, name='utilisateur'),
    path('groupes/', views.groupes_view, name='groupes'),
    
]