from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path('home',views.home ,name='home'), # Par defaut 
    #path('home/<str:param>',views.home ,name='home'),
    path("home", views.HomeView.as_view(), name="home"),
    path("home/<str:param>", views.HomeView.as_view()),
    # path("contact/<str:param>", views.ContactView.as_view()),
    path("about/<str:param>", views.AboutView.as_view()),
    path("contact", views.ContactView, name="contact"),
    path("about", views.AboutView.as_view(), name="about"),
    #path("about", views.about, name="about"),
    path("products", views.ProduitListView.as_view(), name="lst_prdts"),
    path("products/<pk>", views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("categories/<pk>", views.CategorieDetailView.as_view(), name="dtl_ctd"),
    path("status/<pk>", views.StatusDetailView.as_view(), name="dtl_status"),
    path("rayons/<pk>", views.RayonDetailView.as_view(), name="dtl_rayon"),
    path("categories", views.CategorieListView.as_view(), name="lst_ctds"),
    path("rayons", views.RayonListView.as_view(), name="lst_rayons"),
    path("status", views.StatusListView.as_view(), name="lst_status"),
    path('login', views.ConnectView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.DisconnectView.as_view(), name='logout'),
    path('email-sent', views.ConfirmationEmailView.as_view(), name="email-sent")
]
