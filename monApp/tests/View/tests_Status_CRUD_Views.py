from django.test import TestCase
from django.urls import reverse
from monApp.models import Status
from django.contrib.auth.models import User


class StatusCreateViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_Status_create_view_get(self):
        response = self.client.get(reverse('crt_status')) # Utilisation du nom de l'URL
        self.assertEqual(response.status_code, 200)
        # Tester que la vue de création renvoie le bon template
        self.assertTemplateUsed(response, 'monApp/create_status.html')
        
    def test_Status_create_view_post_valid(self):
        data = { "libelleStatus": "StatusPourTestCreation", "prixUnitaireProd": 15.0, "dateFab": "2023-01-01" }
        response = self.client.post(reverse('crt_status'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Status.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Status.objects.last().libelleStatus, 'StatusPourTestCreation')
        
class StatusDetailViewTest(TestCase):
    
    def setUp(self):
        self.prod = Status.objects.create(libelleStatus="StatusPourTestDetail")

    def test_Status_detail_view(self):
        response = self.client.get(reverse('dtl_status', args=[self.prod.idStatus]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_status.html')
        # Vérifie que le nom de la Status est affiché
        self.assertContains(response, 'StatusPourTestDetail')
        # Vérifie que l'id associé est affiché
        self.assertContains(response, '1') 

class StatusUpdateViewTest(TestCase):
    
    def setUp(self):
        self.prod = Status.objects.create(libelleStatus="StatusPourTestUpdate")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_Status_update_view_get(self):
        response = self.client.get(reverse('status_chng', args=[self.prod.idStatus]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_status.html')
        
    def test_update_view_post_valid(self):
        self.assertEqual(self.prod.libelleStatus, 'StatusPourTestUpdate')
        data = {'libelleStatus': 'StatusPourTestAfterUpdate', 'prixUnitaireProd': 12.0, 'dateFab': '2023-01-02'}
        response = self.client.post(reverse('status_chng', args=[self.prod.idStatus]), data)
        # Redirection après la mise à jour
        self.assertEqual(response.status_code, 302)
        # Recharger l'objet depuis la base de données
        self.prod.refresh_from_db()
        # Vérifier la mise à jour du nom
        self.assertEqual(self.prod.libelleStatus, 'StatusPourTestAfterUpdate')
        
class StatusDeleteViewTest(TestCase):

    def setUp(self):
        self.prod = Status.objects.create(libelleStatus="StatusPourTesDelete")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
            
    def test_Status_delete_view_get(self):
        response = self.client.get(reverse('dlt_status', args=[self.prod.idStatus]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_status.html')
        
    def test_Status_delete_view_post(self):
        response = self.client.post(reverse('dlt_status', args=[self.prod.idStatus]))
        # Vérifier la redirection après la suppression
        self.assertEqual(response.status_code, 302)
        # Vérifier que l'objet a été supprimé
        self.assertFalse(Status.objects.filter(idStatus=self.prod.idStatus).exists())
        # Vérifier que la redirection est vers la liste des Statuss
        self.assertRedirects(response, reverse('lst_status'))
