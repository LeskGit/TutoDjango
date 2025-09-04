from django.contrib import admin
from .models import Produit, Categorie, Rayon, Status

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "dateFab", "categorie", "status"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateFab"]
    radio_fields = {"status": admin.VERTICAL}
    search_fields = ('intituleProd', 'dateFabProd')
    list_filter = ('status', 'dateFab')


    
class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1
    
class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [ProduitInline]
    
    
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Status)
admin.site.register(Categorie)
admin.site.register(Rayon)