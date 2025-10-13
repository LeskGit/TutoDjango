from django.test import TestCase
from django.urls import reverse
from monApp.models import Rayon
from django.contrib.auth.models import User


class RayonCreateViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_rayon_create_view_get(self):
        response = self.client.get(reverse('crt_rayon'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_rayon.html')
        
    def test_rayon_create_view_post_valid(self):
        data = {"nomRayon": "RayonPourTestCreation"}
        response = self.client.post(reverse('crt_rayon'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Rayon.objects.count(), 1)
        self.assertEqual(Rayon.objects.last().nomRayon, 'RayonPourTestCreation')
        

class RayonDetailViewTest(TestCase):
    
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTestDetail")

    def test_rayon_detail_view(self):
        response = self.client.get(reverse('dtl_rayon', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_rayon.html')
        self.assertContains(response, 'RayonPourTestDetail')
        self.assertContains(response, str(self.rayon.idRayon)) 


class RayonUpdateViewTest(TestCase):
    
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTestUpdate")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_rayon_update_view_get(self):
        response = self.client.get(reverse('rayon_chng', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_rayon.html')
        
    def test_update_view_post_valid(self):
        self.assertEqual(self.rayon.nomRayon, 'RayonPourTestUpdate')
        data = {'nomRayon': 'RayonPourTestAfterUpdate'}
        response = self.client.post(reverse('rayon_chng', args=[self.rayon.idRayon]), data)
        self.assertEqual(response.status_code, 302)
        self.rayon.refresh_from_db()
        self.assertEqual(self.rayon.nomRayon, 'RayonPourTestAfterUpdate')
        

class RayonDeleteViewTest(TestCase):

    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTestDelete")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
            
    def test_rayon_delete_view_get(self):
        response = self.client.get(reverse('dlt_rayon', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_rayon.html')
        
    def test_rayon_delete_view_post(self):
        response = self.client.post(reverse('dlt_rayon', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Rayon.objects.filter(idRayon=self.rayon.idRayon).exists())
        self.assertRedirects(response, reverse('lst_rayons'))
