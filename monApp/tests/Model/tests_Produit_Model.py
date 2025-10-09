from django.test import TestCase
from monApp.models import Categorie, Produit

class ProduitModelTest(TestCase):
    
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        self.prod = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd=777.50, dateFab='2025-10-09', categorie=self.ctgr)
        
    def test_produit_creation(self):
        self.assertEqual(self.prod.intituleProd, "ProduitPourTest")
        self.assertEqual(self.prod.prixUnitaireProd, 777.50)
        self.assertEqual(self.prod.dateFab, '2025-10-09')
        self.assertEqual(self.prod.categorie, self.ctgr)
        
    def test_string_representation(self):
        self.assertEqual(str(self.prod), "ProduitPourTest")

    def test_produit_updating(self):
        self.prod.intituleProd = "ProduitPourTestUpdated"
        self.prod.save()
        
        updated_prod = Produit.objects.get(refProd=self.prod.refProd)
        self.assertEqual(updated_prod.intituleProd, "ProduitPourTestUpdated")
        
    def test_produit_deletion(self):
        self.prod.delete()
        self.assertEqual(Produit.objects.count(), 0)

