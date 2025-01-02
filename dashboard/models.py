from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import Group

# Modèle User
class NormalUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(verbose_name="Numéro de téléphone", max_length=20, default="")
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")

    def __str__(self):
        return self.username

# Modèle Establishment
class Establishment(models.Model):
    owner = models.ForeignKey(NormalUser, on_delete=models.RESTRICT, related_name='establishments', verbose_name="Propriétaire")
    name = models.CharField(verbose_name="Nom", max_length=225)
    manager_name = models.CharField(verbose_name="Nom du manager", max_length=100, null=True, blank=True)
    foundation_date = models.DateField(verbose_name="Date de fondation", null=True, blank=True)
    address = models.CharField(verbose_name="Adresse", max_length=100)
    nif_cin = models.CharField(verbose_name="NIF_CIN", max_length=9, null=True)
    rc_license = models.CharField(verbose_name="RC", max_length=12, blank=True, null=True)
    phone_number = models.CharField(verbose_name="Numéro de téléphone", max_length=20, default="1234567890")
    email = models.EmailField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(verbose_name="Photo de couverture", upload_to="images/establishments", blank=False, null=True)
    establishment_type = models.CharField(verbose_name="Type d'établissement", max_length=100, choices=[('type1', 'Type 1'), ('type2', 'Type 2')], blank=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)], blank=True, null=True)
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)], blank=True, null=True)
    is_verified = models.BooleanField(verbose_name="Vérifié par Foulanzam", default=False)
    is_available = models.BooleanField(verbose_name="Disponible", default=True)
    is_open = models.BooleanField(verbose_name="Ouvert", default=True)
    is_managed = models.BooleanField(verbose_name="Géré par Foulanzam", default=False)

    def _str_(self):
        return self.name
    



# Modèle Command 
class Command(models.Model):
    STATUS_CHOICES = [
        ('en cours', 'En Cours'),
        ('annulé', 'Annulé'),
        ('livré', 'Livré'),
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateField()

    def __str__(self):
        return self.name