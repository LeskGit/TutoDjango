from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class HomeViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_home_view(self):
        """Test de la vue sans paramètre"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')
        # Vérifie que le contexte contient bien la valeur par défaut
        self.assertIn('titreh1', response.context)
        self.assertEqual(response.context['titreh1'], 'XiaoPang')

    def test_home_view_with_param(self):
        """Test de la vue avec paramètre explicite"""
        response = self.client.get(reverse('home_param', args=['TestUser']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')
        self.assertIn('titreh1', response.context)
        self.assertEqual(response.context['titreh1'], 'TestUser')

    def test_home_view_post(self):
        """Test du POST sur la vue"""
        response = self.client.post(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')

    def test_home_view_content(self):
        """Vérifie que le rendu contient le bon texte dans le HTML"""
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Hello")  # vérifie présence de 'Hello'
        self.assertContains(response, "XiaoPang")  # valeur par défaut affichée

    def test_home_view_with_param_content(self):
        """Vérifie que le rendu HTML contient le paramètre passé"""
        response = self.client.get(reverse('home_param', args=['Alice']))
        self.assertContains(response, "Hello Alice")
