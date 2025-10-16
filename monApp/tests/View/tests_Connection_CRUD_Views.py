from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthViewsTest(TestCase):

    def setUp(self):
        # Création d’un utilisateur de test
        self.user = User.objects.create_user(username="testuser", password="secret", email="test@example.com")

    # === LOGIN ===
    def test_login_view_get(self):
        """GET sur /login doit renvoyer la page de connexion"""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/page_login.html")

    def test_login_view_post_valid(self):
        """POST avec identifiants valides doit rediriger vers home"""
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "secret"})
        self.assertRedirects(response, reverse("home"))
        # Vérifie que l’utilisateur est bien connecté
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_invalid(self):
        """POST avec identifiants invalides doit rediriger vers register"""
        response = self.client.post(reverse("login"), {"username": "wrong", "password": "bad"})
        self.assertRedirects(response, reverse("register"))

    # === REGISTER ===
    def test_register_view_get(self):
        """GET sur /register doit renvoyer la page d’inscription"""
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/page_register.html")

    def test_register_view_post_valid(self):
        """POST valide sur /register doit créer un utilisateur et afficher la page login"""
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "mail": "newuser@example.com",
            "password": "newpass123",
        })
        self.assertTemplateUsed(response, "monApp/page_login.html")
        self.assertTrue(User.objects.filter(username="newuser").exists())

    # === LOGOUT ===
    def test_logout_view_logs_out_user(self):
        """GET sur /logout doit déconnecter l’utilisateur"""
        self.client.login(username="testuser", password="secret")
        response = self.client.get(reverse("logout"))
        self.assertTemplateUsed(response, "monApp/page_logout.html")
        self.assertFalse(response.wsgi_request.user.is_authenticated)
