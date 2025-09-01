from django.db import models

# Create your models here.
class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=200)

    def __str__(self):
        return self.nomCat

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits", null=True, blank=True)

    def __str__(self):
        return self.intituleProd
    
