from django.shortcuts import render
from django.http import HttpResponse
from monApp.models import Produit, Categorie, Status

# Create your views here.
def home(request, param="Coubeh"):
    return HttpResponse("<h1>Hello " + param +" </h1>")

def contact(request):
    return HttpResponse("<h1>Page Contact Us</h1>")

def about(request):
    return HttpResponse("<h1>Page About Us</h1>")

def listProduits(request):
    prdts = Produit.objects.all()
    html = "<h1>Voici tous les produits :</h1> <ul>"
    for prod in prdts:
        html += "<li>" + prod.intituleProd + "</li>"
    html += "</ul>"
    return HttpResponse(html)

def listCategories(request):
    prdts = Categorie.objects.all()
    html = "<h1>Voici toutes les catégories :</h1> <ul>"
    for prod in prdts:
        html += "<li>" + prod.nomCat + "</li>"
    html += "</ul>"
    return HttpResponse(html)

def listStatus(request):
    prdts = Status.objects.all()
    html = "<h1>Voici tous les status :</h1> <ul>"
    for prod in prdts:
        html += "<li>" + prod.libelleStatus + "</li>"
    html += "</ul>"
    return HttpResponse(html)