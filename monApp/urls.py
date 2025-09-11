from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path('home',views.home ,name='home'), # Par defaut 
    #path('home/<str:param>',views.home ,name='home'),
    path("home", views.HomeView.as_view()),
    path("contact", views.contact, name="contact"),
    path("about", views.AboutView.as_view()),
    #path("about", views.about, name="about"),
    path("products", views.listProduits, name="products"),
    path("categories", views.listCategories, name="categories"),
    path("rayons", views.listRayon, name="rayons"),
    path("status", views.listStatus, name="status"),
    
]
