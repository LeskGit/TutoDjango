from django.test import TestCase
from monApp.models import Contenir, Produit, Rayon
from datetime import date

class ContenirModelTest(TestCase):
    
    def setUp(self):
        self.prod = Produit.objects.create(
            intituleProd="ProduitPourTest",
            prixUnitaireProd=777.50,
            dateFab=date(2025, 10, 9) 
        )
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTest")
        self.contenir = Contenir.objects.create(
            produit=self.prod,
            rayon=self.rayon,
            Qte=5
        )
        
    def test_contenir_creation(self):
        self.assertEqual(self.contenir.produit.intituleProd, "ProduitPourTest")
        self.assertEqual(self.contenir.rayon.nomRayon, "RayonPourTest")
        self.assertEqual(self.contenir.Qte, 5)
        
    def test_string_representation(self):
        expected_str = f"{self.contenir.produit} dans {self.contenir.rayon} (Qte: {self.contenir.Qte})"
        self.assertEqual(str(self.contenir), expected_str)

    def test_contenir_updating(self):
        # Exemple : mise à jour de la quantité
        self.contenir.Qte = 10
        self.contenir.save()
        
        updated_contenir = Contenir.objects.get(id=self.contenir.id)
        self.assertEqual(updated_contenir.Qte, 10)
        
    def test_contenir_deletion(self):
        self.contenir.delete()
        self.assertEqual(Contenir.objects.count(), 0)
