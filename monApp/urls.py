from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home ,name='home'), # Par defaut 
    path('home/<str:param>',views.home ,name='home'),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("products", views.listProduits, name="products"),
    path("categories", views.listCategories, name="categories"),
    path("status", views.listStatus, name="status"),
]
