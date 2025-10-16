from django.test import TestCase
from monApp.forms import ContenirForm
from monApp.models import Contenir, Produit, Rayon

class ContenirFormTest(TestCase):
    
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTest")
        self.prod = Produit.objects.create(
            intituleProd="ProduitPourTest",
            prixUnitaireProd=777.50,
            dateFab='2025-10-09'
        )

    def test_form_valid_data(self):
        form = ContenirForm(data={
            'produit': self.prod.refProd,       # utiliser l'id du produit (clé étrangère)
            'rayon': self.rayon.idRayon,        # idem pour le rayon
            'Qte': 5
        })

        self.assertTrue(form.is_valid())

    def test_form_valid_data_missed(self):
        form = ContenirForm(data={'Qte': 5})
        self.assertFalse(form.is_valid())
        self.assertIn('produit', form.errors)
        self.assertEqual(form.errors['produit'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = ContenirForm(data={
            'produit': self.prod.refProd,
            'rayon': self.rayon.idRayon,
            'Qte': 5
        })

        self.assertTrue(form.is_valid())
        contenir = form.save()
        self.assertEqual(contenir.produit, self.prod)
        self.assertEqual(contenir.rayon, self.rayon)
        self.assertEqual(contenir.Qte, 5)
