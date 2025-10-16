from rest_framework import serializers
from monApp.models import Categorie, Contenir, Produit, Rayon, Status



class CategorieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categorie
        fields = ["idCat", "nomCat"]
        
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ["refProd", "intituleProd", "dateFab", "categorie"]
        
class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = ["idRayon", "nomRayon"]
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["idStatus", "libelleStatus"]

class ContenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenir
        fields = ["rayon", "produit", "Qte"]