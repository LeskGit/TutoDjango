from django.test import TestCase
from monApp.models import Rayon

class RayonModelTest(TestCase):
    
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTest")
        
    def test_rayon_creation(self):
        self.assertEqual(self.rayon.nomRayon, "RayonPourTest")
        
    def test_string_representation(self):
        self.assertEqual(str(self.rayon), "RayonPourTest")

    def test_rayon_updating(self):
        self.rayon.nomRayon = "RayonPourTestUpdated"
        self.rayon.save()
        
        updated_rayon = Rayon.objects.get(idRayon=self.rayon.idRayon)
        self.assertEqual(updated_rayon.nomRayon, "RayonPourTestUpdated")
        
    def test_rayon_deletion(self):
        self.rayon.delete()
        self.assertEqual(Rayon.objects.count(), 0)

