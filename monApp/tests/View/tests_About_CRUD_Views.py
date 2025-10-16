from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AboutViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_about_view(self):
        """Test GET sans paramètre"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')
        self.assertIn('titreh1', response.context)
        self.assertEqual(response.context['titreh1'], 'XiaoPang')
        self.assertIn('desc', response.context)
        self.assertEqual(response.context['desc'], 'Axel Meunier, BUT 3, Loup')

    def test_about_view_with_param(self):
        """Test GET avec paramètre"""
        response = self.client.get(reverse('about_param', args=['Jean']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')
        self.assertEqual(response.context['titreh1'], 'Jean')
        self.assertEqual(response.context['desc'], 'Axel Meunier, BUT 3, Loup')

    def test_about_view_post(self):
        """Test POST simple"""
        response = self.client.post(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')

    def test_about_view_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, "Hello XiaoPang !!!")

    def test_about_view_with_param_content(self):
        response = self.client.get(reverse('about_param', args=['Alice']))
        self.assertContains(response, "Hello Alice !!!")
