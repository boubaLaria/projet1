from django.db import models
from django import forms
from phone_field import PhoneField
from django.core.validators import RegexValidator, EmailValidator

"""
    Creation du model client pour la table client
"""
class Client(models.Model):
    GENRE=(
        ('M','Masculin'),
        ('F','Feminin'),
    )
    nom_client=models.CharField(max_length=50)
    prenom_client=models.CharField(max_length=100)
    genre=models.CharField(max_length=1, choices=GENRE)
    phone_regex = RegexValidator(
        regex=r'^\d{9}$',
        message="Le numero doit contenir 9 chiffres comme: 622678756"
    )
    telephone = models.CharField(
        validators=[phone_regex],
        verbose_name=("Mobile phone"),
        max_length=17, blank=True, null=True
    )
    email=models.EmailField(max_length=100, unique=True)
    password=models.CharField(max_length=30)
    adresse=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: nom=:{self.nom_client}, {self.prenom_client}"

class Plat(models.Model):
    nom_plat=models.CharField(max_length=100)
    prix=models.IntegerField()
    type_plat=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    photo = models.ImageField(
        verbose_name=("Photo"), 
        upload_to='photos/', 
        default='photos/assiette.png'
    )
    def __str__(self):
        return f"{self.nom_plat}, {self.prix}, {self.type_plat}, {self.description}"

class Restaurant(models.Model):
     nom=models.CharField(max_length=100)
     commune=models.CharField(max_length=100)  
     quartier=models.CharField(max_length=100)

     def __str__(self):
        return f"{self.nom}, {self.commune}, {self.quartier}"

class Commande(models.Model):
    STATUS=(('Livre','Livré'),('Attente','En Attente'))
    date_com=models.DateField('Date')
    status=models.CharField(max_length=20,choices=STATUS)
    plat=models.ManyToManyField(Plat)
    id_client=models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_com}, {self.status}, {self.id_client}"
