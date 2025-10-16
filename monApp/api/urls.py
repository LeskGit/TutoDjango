from monApp.views import CategorieListAPI, ContenirListAPI, ProduitListAPI, RayonListAPI, StatusListAPI
from django.urls import path

urlpatterns = [path('categories/', CategorieListAPI.as_view(), name="api-lst-ctgrs"),
               path('products/', ProduitListAPI.as_view(), name="api-lst-prdts"),
               path('rayons/', RayonListAPI.as_view(), name="api-lst-rayons"),
               path('status/', StatusListAPI.as_view(), name="api-lst-status"),
               path('contenirs/', ContenirListAPI.as_view(), name="api-lst-contenirs"),
               ]