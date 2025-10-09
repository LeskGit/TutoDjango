from django.test import TestCase
from monApp.forms import ContenirForm
from monApp.models import Contenir, Produit, Rayon

class ContenirFormTest(TestCase):
    
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTest")
        self.prod = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd=777.50, dateFab='2025-10-09')

    
    def test_form_valid_data(self):
        form = ContenirForm(data = {
            'produit': self.prod.refProd,
            'rayon': self.rayon.idRayon,
            'Qte': 5
        })

        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_missed(self):
        form = ContenirForm(data = {'produit': None})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('produit', form.errors) # Le champ 'nomContenir' doit contenir une erreur
        self.assertEqual(form.errors['produit'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = ContenirForm(data = {
            'produit': self.prod.refProd,
            'rayon': self.rayon.idRayon,
            'Qte': 5
        })

        self.assertTrue(form.is_valid())
        contenir = form.save()
        self.assertEqual(contenir.produit, self.prod.refProd)
        self.assertEqual(contenir.Qte, 5)