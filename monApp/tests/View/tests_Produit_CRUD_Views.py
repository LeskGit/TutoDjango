from django.test import TestCase
from django.urls import reverse
from monApp.models import Produit
from django.contrib.auth.models import User


class ProduitCreateViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_Produit_create_view_get(self):
        response = self.client.get(reverse('crt_prdt')) # Utilisation du nom de l'URL
        self.assertEqual(response.status_code, 200)
        # Tester que la vue de création renvoie le bon template
        self.assertTemplateUsed(response, 'monApp/create_produit.html')
        
    def test_Produit_create_view_post_valid(self):
        data = { "intituleProd": "ProduitPourTestCreation", "prixUnitaireProd": 15.0, "dateFab": "2023-01-01" }
        response = self.client.post(reverse('crt_prdt'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Produit.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Produit.objects.last().intituleProd, 'ProduitPourTestCreation')
        
class ProduitDetailViewTest(TestCase):
    
    def setUp(self):
        self.prod = Produit.objects.create(intituleProd="ProduitPourTestDetail", prixUnitaireProd=10.0, dateFab="2023-01-01")

    def test_Produit_detail_view(self):
        response = self.client.get(reverse('dtl_prdt', args=[self.prod.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_produit.html')
        # Vérifie que le nom de la Produit est affiché
        self.assertContains(response, 'ProduitPourTestDetail')
        # Vérifie que l'id associé est affiché
        self.assertContains(response, '1') 

class ProduitUpdateViewTest(TestCase):
    
    def setUp(self):
        self.prod = Produit.objects.create(intituleProd="ProduitPourTestUpdate", prixUnitaireProd=10.0, dateFab="2023-01-01")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_Produit_update_view_get(self):
        response = self.client.get(reverse('prdt_chng', args=[self.prod.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_produit.html')
        
    def test_update_view_post_valid(self):
        self.assertEqual(self.prod.intituleProd, 'ProduitPourTestUpdate')
        data = {'intituleProd': 'ProduitPourTestAfterUpdate', 'prixUnitaireProd': 12.0, 'dateFab': '2023-01-02'}
        response = self.client.post(reverse('prdt_chng', args=[self.prod.refProd]), data)
        # Redirection après la mise à jour
        self.assertEqual(response.status_code, 302)
        # Recharger l'objet depuis la base de données
        self.prod.refresh_from_db()
        # Vérifier la mise à jour du nom
        self.assertEqual(self.prod.intituleProd, 'ProduitPourTestAfterUpdate')
        
class ProduitDeleteViewTest(TestCase):
    
        def setUp(self):
            self.prod = Produit.objects.create(intituleProd="ProduitPourTesDelete", prixUnitaireProd=10.0, dateFab="2023-01-01")
            self.user = User.objects.create_user(username='testuser', password='secret')
            self.client.login(username='testuser', password='secret')
            
        def test_Produit_delete_view_get(self):
            response = self.client.get(reverse('dlt_prdts', args=[self.prod.refProd]))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'monApp/delete_produit.html')
            
        def test_Produit_delete_view_post(self):
            response = self.client.post(reverse('dlt_prdts', args=[self.prod.refProd]))
            # Vérifier la redirection après la suppression
            self.assertEqual(response.status_code, 302)
            # Vérifier que l'objet a été supprimé
            self.assertFalse(Produit.objects.filter(refProd=self.prod.refProd).exists())
            # Vérifier que la redirection est vers la liste des produits
            self.assertRedirects(response, reverse('lst_prdts'))
