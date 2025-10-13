from django.test import TestCase
from django.urls import reverse
from monApp.models import Contenir, Rayon, Produit
from django.contrib.auth.models import User


class ContenirCreateViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.rayon = Rayon.objects.create(nomRayon="RayonTest")
        self.produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10.0,
            dateFab="2023-01-01"
        )

    def test_contenir_create_view_get(self):
        url = reverse('cntnr-crt', args=[self.rayon.idRayon])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_contenir.html')

    def test_contenir_create_view_post_valid(self):
        url = reverse('cntnr-crt', args=[self.rayon.idRayon])
        data = {
            "produit": self.produit.refProd,
            "Qte": 5
        }
        response = self.client.post(url, data)
        # Redirection vers la page détail du rayon
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contenir.objects.count(), 1)
        contenir = Contenir.objects.last()
        self.assertEqual(contenir.produit, self.produit)
        self.assertEqual(contenir.rayon, self.rayon)
        self.assertEqual(contenir.Qte, 5)


class ContenirUpdateViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

        self.rayon = Rayon.objects.create(nomRayon="RayonTestUpdate")
        self.produit = Produit.objects.create(
            intituleProd="ProduitUpdate",
            prixUnitaireProd=20.0,
            dateFab="2023-01-01"
        )
        self.contenir = Contenir.objects.create(produit=self.produit, rayon=self.rayon, Qte=10)
        
    def test_contenir_update_view_get(self):
        url = reverse('cntnr-chng', args=[self.contenir.rayon.idRayon])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_contenir.html')
        
    def test_contenir_update_view_post_valid(self):
        url = reverse('cntnr-chng', args=[self.contenir.rayon.idRayon])
        data = {
            "produit": self.produit.refProd,
            "rayon": self.rayon.idRayon,
            "Qte": 15
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.contenir.refresh_from_db()
        self.assertEqual(self.contenir.Qte, 15)
        

class ContenirDeleteViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

        self.rayon = Rayon.objects.create(nomRayon="RayonTestDelete")
        self.produit = Produit.objects.create(
            intituleProd="ProduitDelete",
            prixUnitaireProd=30.0,
            dateFab="2023-01-01"
        )
        self.contenir = Contenir.objects.create(produit=self.produit, rayon=self.rayon, Qte=8)
            
    def test_contenir_delete_view_get(self):
        url = reverse('cntnr-dlt', args=[self.contenir.rayon.idRayon])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_contenir.html')
        
    def test_contenir_delete_view_post(self):
        url = reverse('cntnr-dlt', args=[self.contenir.rayon.idRayon])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contenir.objects.filter(id=self.contenir.rayon.idRayon).exists())
        self.assertRedirects(response, reverse('lst_rayons'))
