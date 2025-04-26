from django.db import models

# Create your models here.




class Hebergement(models.Model):
    TYPE_CHOICES = [
        ('hotel', 'Hôtel'),
        ('riad', 'Riad'),
        ('appartement', 'Appartement'),
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField()
    ville = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    prix_par_nuit = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom





class Logement(models.Model):
    TYPE_CHOICES = [
        ('hotel', 'Hôtel'),
        ('riad', 'Riad'),
        ('appartement', 'Appartement'),
    ]

    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    type_logement = models.CharField(max_length=20, choices=TYPE_CHOICES)
    prix_par_nuit = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='logements/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
    



class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    prix_par_jour = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='voitures/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marque} {self.modele}"
    



class Restaurant(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    type_cuisine = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurants/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom






from django.contrib.auth.models import User

class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, null=True, blank=True)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Réservation par {self.utilisateur.username} du {self.date_debut} au {self.date_fin}"





