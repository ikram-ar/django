from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('etablissement/', views.etablissement_view, name='etablissement'),
    path('utilisateur/', views.utilisateur_view, name='utilisateur'),
    path('groupes/', views.groupes_view, name='groupes'),

    # URL patterns for users
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    # URL patterns for Établissement (Establishment)
    path('add_etablissement/', views.add_etablissement, name='add_etablissement'),
    path('edit_etablissement/<int:etablissement_id>/', views.edit_etablissement, name='edit_etablissement'),
    path('delete_etablissement/<int:etablissement_id>/', views.delete_etablissement, name='delete_etablissement'),

    # URL patterns for Groupes
    path('add_usergroup/', views.usergroup_add, name='add_usergroup'),
    path('edit_usergroup/<int:pk>/', views.usergroup_edit, name='edit_usergroup'),
    path('delete_usergroup/<int:pk>/', views.usergroup_delete, name='delete_usergroup'),
]