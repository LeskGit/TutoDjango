from django.shortcuts import render
from django.http import HttpResponse, Http404
from monApp.models import Produit, Categorie, Status, Rayon
from django.views.generic import *


class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
    def get_context_data(self, **kwargs):
        param = self.kwargs.get('param')
        if param == None:
            param = "XiaoPang"
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = param
        return context


class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        param = self.kwargs.get('param')
        if param == None:
            param = "XiaoPang"
        context = super(AboutView, self).get_context_data(**kwargs)
        context["titreh1"] = param
        context["desc"] = "Axel Meunier, BUT 3, Loup"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        param = self.kwargs.get('param')
        if param == None:
            param = "XiaoPang"
        context = super(ContactView, self).get_context_data(**kwargs)
        context["titreh1"] = param
        context["desc"] = "axel.meunier49@gmail.com"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    # queryset = Produit.objects.filter(id=2)
    
    def get_queryset(self ) :
        return Produit.objects.order_by("prixUnitaireProd")
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/categories_produits.html"
    context_object_name = "ctds"
    # queryset = Categorie.objects.filter(id=2)
    
    def get_queryset(self ) :
        return Categorie.objects.order_by("nomCat")
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes categories"
        return context

class StatusListView(ListView):
    model = Status
    template_name = "monApp/list_status.html"
    context_object_name = "status"
    # queryset = Status.objects.filter(id=2)
    
    def get_queryset(self ) :
        return Status.objects.order_by("libelleStatus")
    
    def get_context_data(self, **kwargs):
        context = super(StatusListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes status"
        return context
    
class RayonListView(ListView):
    model = Status
    template_name = "monApp/list_rayons.html"
    context_object_name = "status"
    # queryset = Status.objects.filter(id=2)
    
    def get_queryset(self ) :
        return Rayon.objects.order_by("nomRayon")
    
    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        return context


class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    
    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
        


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "ctds"
    
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context
        


class StatusDetailView(DetailView):
    model = Status
    template_name = "monApp/detail_status.html"
    context_object_name = "status"
    
    def get_context_data(self, **kwargs):
        context = super(StatusDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du status"
        return context
        
class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayons"
    
    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context
        



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