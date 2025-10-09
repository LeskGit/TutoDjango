from django.test import TestCase
from monApp.forms import StatusForm
from monApp.models import Status

class StatusFormTest(TestCase):
    
    def test_form_valid_data(self):
        form = StatusForm(data = {'libelleStatus': 'StatusPourTest'})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_too_long(self):
        long_name = 'S' * 101  # 101 caractères > max_length=100
        form = StatusForm(data={'libelleStatus': long_name})
        
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('libelleStatus', form.errors)  # Le champ doit contenir une erreur
        self.assertEqual(
            form.errors['libelleStatus'],
            [f'Assurez-vous que cette valeur comporte au plus 100 caractères (actuellement {len(long_name)}).']
        )

    def test_form_valid_data_missed(self):
        form = StatusForm(data = {'libelleStatus': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('libelleStatus', form.errors) # Le champ 'libelleStatus' doit contenir une erreur
        self.assertEqual(form.errors['libelleStatus'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = StatusForm(data = {'libelleStatus': 'StatusPourTest'})
        self.assertTrue(form.is_valid())
        status = form.save()
        self.assertEqual(status.libelleStatus, 'StatusPourTest')
        self.assertEqual(status.idStatus, 1)