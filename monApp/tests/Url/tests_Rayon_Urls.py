from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Rayon
from monApp.views import RayonCreateView, RayonDeleteView, RayonListView, RayonDetailView, RayonUpdateView
from django.contrib.auth.models import User


class RayonUrlsTest(TestCase):
    
    def setUp(self):
        self.Rayon = Rayon.objects.create(nomRayon="RayonPourTest") 
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    
    def test_Rayon_list_url_is_resolved(self):
        url = reverse('lst_rayons')
        self.assertEqual(resolve(url).view_name, 'lst_rayons')
        self.assertEqual(resolve(url).func.view_class,RayonListView)
        
    def test_Rayon_detail_url_is_resolved(self):
        url = reverse('dtl_rayon', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_rayon')
        self.assertEqual(resolve(url).func.view_class, RayonDetailView)
        
    def test_Rayon_create_url_is_resolved(self):
        url = reverse('crt_rayon')
        self.assertEqual(resolve(url).view_name, 'crt_rayon')
        self.assertEqual(resolve(url).func.view_class, RayonCreateView)

    def test_Rayon_update_url_is_resolved(self):
        url = reverse('rayon_chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'rayon_chng')
        self.assertEqual(resolve(url).func.view_class, RayonUpdateView)
        
    def test_Rayon_delete_url_is_resolved(self):
        url = reverse('dlt_rayon', args=[1])
        self.assertEqual(resolve(url).view_name, 'dlt_rayon')
        self.assertEqual(resolve(url).func.view_class, RayonDeleteView)

    def test_Rayon_list_response_code(self):
        response = self.client.get(reverse('lst_rayons'))
        self.assertEqual(response.status_code, 200)

    def test_Rayon_detail_response_code(self):
        url = reverse('dtl_rayon', args=[self.Rayon.idRayon]) #refRayon existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_Rayon_detail_response_code_KO(self):
        url = reverse('dtl_rayon', args=[9999]) # refRayon non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_Rayon_create_response_code_OK(self):
        response = self.client.get(reverse('crt_rayon'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_after_rayon_creation(self):
        response = self.client.post(reverse('crt_rayon'), {'nomRayon': 'RayonPourTestRedirectionCreation'} )
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, f'/monApp/rayons/{self.Rayon.idRayon + 1}')
    
    def test_redirect_after_rayon_updating(self):
        response = self.client.post(reverse('rayon_chng', args=[self.Rayon.idRayon]),
        data={"nomRayon": "RayonPourTestRedirectionMaj"})
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, f'/monApp/rayons/{self.Rayon.idRayon}')
    
    def test_redirect_after_rayon_deletion(self):
        response = self.client.post(reverse('dlt_rayon', args=[self.Rayon.pk]))
        # Vérifie qu'on a bien une redirection
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lst_rayons'))
        # Vérifie que le rayon a bien été supprimé de la base
        self.assertFalse(Rayon.objects.filter(pk=self.Rayon.pk).exists())