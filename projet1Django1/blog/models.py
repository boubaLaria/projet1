from django.db import models


class Client(models.Model):
    nom_client=models.CharField(max_length=50)
    prenom_client=models.CharField(max_length=100)
    genre=models.CharField(max_length=2)
    telephone=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    adresse=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: nom=:{self.nom_client}, {self.prenom_client}"

class Commande(models.Model):
    date_com=models.DateField('date published')
    status=models.CharField(max_length=20)
    id_client=models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_com}, {self.status}, {self.id_client}"

class Plat(models.Model):
    nom_plat=models.CharField(max_length=100)
    prix=models.IntegerField()
    type_plat=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    photo=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom_plat}, {self.prix}, {self.type_plat}, {self.description}"

class Restaurant(models.Model):
     nom=models.CharField(max_length=100)
     commune=models.CharField(max_length=100)  
     quartier=models.CharField(max_length=100)

     def __str__(self):
        return f"{self.nom}, {self.commune}, {self.quartier}"

class Repas(models.Model):
    id_plat=models.ForeignKey(Plat, on_delete=models.CASCADE)
    id_cmd=models.ForeignKey(Commande, on_delete=models.CASCADE)
    nbr_plat=models.IntegerField()

class List_plat(models.Model):
    id_plat=models.ForeignKey(Plat, on_delete=models.CASCADE)
    id_restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)