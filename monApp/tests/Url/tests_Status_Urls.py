from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Status
from monApp.views import StatusCreateView, StatusDeleteView, StatusListView, StatusDetailView, StatusUpdateView
from django.contrib.auth.models import User


class StatusUrlsTest(TestCase):
    
    def setUp(self):
        self.status = Status.objects.create(libelleStatus="StatusPourTest") 
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    
    def test_Status_list_url_is_resolved(self):
        url = reverse('lst_status')
        self.assertEqual(resolve(url).view_name, 'lst_status')
        self.assertEqual(resolve(url).func.view_class,StatusListView)
        
    def test_Status_detail_url_is_resolved(self):
        url = reverse('dtl_status', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_status')
        self.assertEqual(resolve(url).func.view_class, StatusDetailView)
        
    def test_Status_create_url_is_resolved(self):
        url = reverse('crt_status')
        self.assertEqual(resolve(url).view_name, 'crt_status')
        self.assertEqual(resolve(url).func.view_class, StatusCreateView)

    def test_Status_update_url_is_resolved(self):
        url = reverse('status_chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'status_chng')
        self.assertEqual(resolve(url).func.view_class, StatusUpdateView)
        
    def test_Status_delete_url_is_resolved(self):
        url = reverse('dlt_status', args=[1])
        self.assertEqual(resolve(url).view_name, 'dlt_status')
        self.assertEqual(resolve(url).func.view_class, StatusDeleteView)

    def test_Status_list_response_code(self):
        response = self.client.get(reverse('lst_status'))
        self.assertEqual(response.status_code, 200)

    def test_Status_detail_response_code(self):
        url = reverse('dtl_status', args=[self.status.idStatus]) #refstatus existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_Status_detail_response_code_KO(self):
        url = reverse('dtl_status', args=[9999]) # refstatus non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_Status_create_response_code_OK(self):
        response = self.client.get(reverse('crt_status'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_after_status_creation(self):
        response = self.client.post(reverse('crt_status'), {'libelleStatus': 'StatusPourTestRedirectionCreation'} )
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, '/monApp/status/2')
        
    def test_redirect_after_status_updating(self):
        response = self.client.post(reverse('status_chng', args=[self.status.idStatus]),
        data={"libelleStatus": "StatusPourTestRedirectionMaj"})
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, f'/monApp/status/{self.status.idStatus}')

    def test_redirect_after_status_deletion(self):
        response = self.client.post(reverse('dlt_status', args=[self.status.pk]))
        # Vérifie qu'on a bien une redirection
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lst_status'))
        # Vérifie que le statut a bien été supprimé de la base
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())