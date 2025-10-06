from django.test import TestCase
from monApp.models import Categorie

class CategorieModelTest(TestCase):
    
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        
    def test_categorie_creation(self):
        self.assertEqual(self.ctgr.nomCat, "CategoriePourTest")
        
    def test_string_representation(self):
        self.assertEqual(str(self.ctgr), "CategoriePourTest")

    def test_categorie_updating(self):
        self.ctgr.nomCat = "CategoriePourTestUpdated"
        self.ctgr.save()
        
        updated_ctgr = Categorie.objects.get(idCat=self.ctgr.idCat)
        self.assertEqual(updated_ctgr.nomCat, "CategoriePourTestUpdated")
        
    def test_categorie_deletion(self):
        self.ctgr.delete()
        self.assertEqual(Categorie.objects.count(), 0)

