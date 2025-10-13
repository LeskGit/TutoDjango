from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Produit
from monApp.views import ProduitCreateView, ProduitDeleteView, ProduitListView, ProduitDetailView, ProduitUpdateView
from django.contrib.auth.models import User


class ProduitUrlsTest(TestCase):
    
    def setUp(self):
        self.prod = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd=10.0, dateFab="2023-01-01") 
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    
    def test_Produit_list_url_is_resolved(self):
        url = reverse('lst_prdts')
        self.assertEqual(resolve(url).view_name, 'lst_prdts')
        self.assertEqual(resolve(url).func.view_class,ProduitListView)
        
    def test_Produit_detail_url_is_resolved(self):
        url = reverse('dtl_prdt', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_prdt')
        self.assertEqual(resolve(url).func.view_class, ProduitDetailView)
        
    def test_Produit_create_url_is_resolved(self):
        url = reverse('crt_prdt')
        self.assertEqual(resolve(url).view_name, 'crt_prdt')
        self.assertEqual(resolve(url).func.view_class, ProduitCreateView)

    def test_Produit_update_url_is_resolved(self):
        url = reverse('prdt_chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'prdt_chng')
        self.assertEqual(resolve(url).func.view_class, ProduitUpdateView)
        
    def test_Produit_delete_url_is_resolved(self):
        url = reverse('dlt_prdts', args=[1])
        self.assertEqual(resolve(url).view_name, 'dlt_prdts')
        self.assertEqual(resolve(url).func.view_class, ProduitDeleteView)

    def test_Produit_list_response_code(self):
        response = self.client.get(reverse('lst_prdts'))
        self.assertEqual(response.status_code, 200)

    def test_Produit_detail_response_code(self):
        url = reverse('dtl_prdt', args=[self.prod.refProd]) #refProd existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_Produit_detail_response_code_KO(self):
        url = reverse('dtl_prdt', args=[9999]) # refProd non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_Produit_create_response_code_OK(self):
        response = self.client.get(reverse('crt_prdt'))
        self.assertEqual(response.status_code, 200)
