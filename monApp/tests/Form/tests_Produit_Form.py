from django.test import TestCase
from monApp.forms import ProduitForm
from monApp.models import Categorie, Produit

class ProduitFormTest(TestCase):
    
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
    
    def test_form_valid_data(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest', 'prixUnitaireProd': 11.0, 'dateFab': '2025-02-01', 'categorie': 1})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_too_long(self):
        long_name = 'P' * 201  # > max_length=200
        form = ProduitForm(data={
            'intituleProd': long_name,
            'prixUnitaireProd': 11.0,
            'dateFab': '2025-02-01',
            'categorie': 1
        })

        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors)  # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(
            form.errors['intituleProd'],
            [f'Assurez-vous que cette valeur comporte au plus 200 caractères (actuellement {len(long_name)}).']
        )

    def test_form_valid_data_missed(self):
        form = ProduitForm(data = {'intituleProd': '', 'prixUnitaireProd': 11.0, 'dateFab': '2025-02-01', 'categorie': 1})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest', 'prixUnitaireProd': 11.0, 'dateFab': '2025-02-01', 'categorie': 1})
        self.assertTrue(form.is_valid())
        prod = form.save()
        self.assertEqual(prod.intituleProd, 'ProduitPourTest')
        self.assertEqual(prod.refProd, 1)