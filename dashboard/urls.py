from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('etablissement/', views.etablissement_view, name='etablissement'),
    path('utilisateur/', views.utilisateur_view, name='utilisateur'),
    path('groupes/', views.groupes_view, name='groupes'),  # List groups

    # URL patterns for Utilisateur (User)
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    # URL patterns for Établissement (Establishment)
    path('add_etablissement/', views.add_etablissement, name='add_etablissement'),
    path('edit_etablissement/<int:etablissement_id>/', views.edit_etablissement, name='edit_etablissement'),
    path('delete_etablissement/<int:etablissement_id>/', views.delete_etablissement, name='delete_etablissement'),

    # URL patterns for Groupe (Group)
    path('add_groupe/', views.add_groupe, name='add_groupe'),  # URL for adding a group
    path('edit_groupe/<int:groupe_id>/', views.edit_groupe, name='edit_groupe'),  # URL for editing a group
    path('delete_groupe/<int:groupe_id>/', views.delete_groupe, name='delete_groupe'),
]
