from django.shortcuts import render
from django.http import HttpResponse, Http404
from monApp.models import Produit, Categorie, Status, Rayon
from django.views.generic import *


class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "monApp/about.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["titreh1"] = "About us..."
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
        


# Create your views here.
def home(request, param="Coubeh"):
    return HttpResponse("<h1>Hello " + param +" </h1>")

def contact(request):
    return render(request, 'monApp/contact.html')

def about(request):
    return render(request, 'monApp/about.html')

def listProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html', {'prdts' : prdts})

def listCategories(request):
    ctds = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html', {'ctds' : ctds})

def listStatus(request):
    stats = Status.objects.all()
    return render(request, 'monApp/list_status.html', {'stats' : stats})

def listRayon(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html', {'rayons' : rayons})