from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path('home',views.home ,name='home'), # Par defaut 
    #path('home/<str:param>',views.home ,name='home'),
    path("home", views.HomeView.as_view()),
    path("home/<str:param>", views.HomeView.as_view()),
    path("contact/<str:param>", views.ContactView.as_view()),
    path("about/<str:param>", views.AboutView.as_view()),
    path("contact", views.ContactView.as_view()),
    path("about", views.AboutView.as_view()),
    #path("about", views.about, name="about"),
    path("products", views.ProduitListView.as_view(), name="lst_prdts"),
    path("products/<pk>", views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("categories/<pk>", views.CategorieDetailView.as_view(), name="dtl_ctd"),
    path("status/<pk>", views.StatusDetailView.as_view(), name="dtl_status"),
    path("rayons/<pk>", views.RayonDetailView.as_view(), name="dtl_rayon"),
    path("categories", views.listCategories, name="lst_ctds"),
    path("rayons", views.listRayon, name="lst_rayons"),
    path("status", views.listStatus, name="lst_status"),
    
]
