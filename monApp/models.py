from django.db import models
from django.utils import timezone

# Create your models here.
class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=200)

    def __str__(self):
        return self.nomCat
    
class Status(models.Model):
    idStatus = models.AutoField(primary_key=True)
    libelleStatus = models.CharField(max_length=200)
    
    def __str__(self):
        return self.libelleStatus

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    dateFab = models.DateField(default=timezone.now)
    
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits", null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status", null=True, blank=True)

    def __str__(self):
        return self.intituleProd
    

class Rayon(models.Model):
    idRayon = models.AutoField(primary_key=True)
    nomRayon = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nomRayon

    
class Contenir(models.Model):
    quantite = models.IntegerField(default=0)
    rayon = models.ForeignKey(Rayon, on_delete=models.CASCADE, related_name="rayons")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="produits")
    
    def __str__(self):
        return f"Contient : {self.quantite}"

    