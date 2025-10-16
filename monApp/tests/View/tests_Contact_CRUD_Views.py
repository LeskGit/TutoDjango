from django.test import TestCase
from django.urls import reverse
from django.core import mail
from monApp.forms import ContactUsForm


class ContactViewTest(TestCase):

    def test_contact_view_get(self):
        """Test GET : la page s'affiche avec le bon titre et le formulaire"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')
        self.assertContains(response, "Contact us !")
        self.assertIsInstance(response.context['form'], ContactUsForm)

    def test_contact_view_post_invalid(self):
        """Test POST invalide (email manquant) : doit réafficher le formulaire"""
        data = {"name": "Axel", "message": "Hello"}
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')
        self.assertIsInstance(response.context['form'], ContactUsForm)
        self.assertTrue(response.context['form'].errors)

    def test_contact_view_post_valid(self):
        """Test POST valide : doit envoyer un email et rediriger"""
        data = {
            "name": "Axel",
            "email": "axel@test.com",
            "message": "Bonjour, ceci est un test.",
        }
        response = self.client.post(reverse('contact'), data)
        # Vérifie redirection après succès
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('email-sent'))
        # Vérifie qu'un mail a bien été envoyé
        self.assertEqual(len(mail.outbox), 1)
        sent_mail = mail.outbox[0]
        self.assertIn("Axel", sent_mail.subject)
        self.assertIn("Bonjour, ceci est un test.", sent_mail.body)
        self.assertEqual(sent_mail.to, ['admin@monApp.com'])

    def test_contact_view_form_in_context(self):
        """Le formulaire doit toujours être présent dans le contexte (GET)"""
        response = self.client.get(reverse('contact'))
        self.assertIn('form', response.context)

    def test_contact_view_title(self):
        """Vérifie le titre affiché"""
        response = self.client.get(reverse('contact'))
        self.assertContains(response, "Contact us !")

