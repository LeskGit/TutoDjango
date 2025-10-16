from django.forms import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from monApp.forms import ContactUsForm, ProduitForm, CategorieForm, StatusForm, RayonForm, ContenirForm
from monApp.models import Contenir, Produit, Categorie, Status, Rayon
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Count, Prefetch
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required





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

# class ContactView(TemplateView):
#     template_name = "monApp/page_home.html"
    
#     def get_context_data(self, **kwargs):
#         param = self.kwargs.get('param')
#         if param == None:
#             param = "XiaoPang"
#         context = super(ContactView, self).get_context_data(**kwargs)
#         context["titreh1"] = param
#         context["desc"] = "axel.meunier49@gmail.com"
#         return context
    
#     def post(self, request, **kwargs):
#         return render(request, self.template_name)
    
def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via TutoDjango Contact form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monApp.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})

# def ProduitCreate(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST)
#         if form.is_valid():
#             prdt = form.save()
#             return redirect("dtl_prdt", prdt.refProd)
#     else:
#         form = ProduitForm()
#     return render(request, "monApp/create_produit.html", {'form': form})

@method_decorator(login_required, name='dispatch')   
class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

@method_decorator(login_required, name='dispatch')   
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

@method_decorator(login_required, name='dispatch')   
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')
    
@method_decorator(login_required, name='dispatch')   
class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_ctd', cat.idCat)

@method_decorator(login_required, name='dispatch')   
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_ctd', cat.idCat)

@method_decorator(login_required, name='dispatch')   
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_ctds')

@method_decorator(login_required, name='dispatch')   
class RayonCreateView(CreateView):
    model = Categorie
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)

@method_decorator(login_required, name='dispatch')   
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)

@method_decorator(login_required, name='dispatch')   
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')

@method_decorator(login_required, name='dispatch')   
class StatusCreateView(CreateView):
    model = Status
    form_class=StatusForm
    template_name = "monApp/create_status.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        status = form.save()
        return redirect('dtl_status', status.idStatus)

@method_decorator(login_required, name='dispatch')   
class StatusUpdateView(UpdateView):
    model = Status
    form_class= StatusForm
    template_name = "monApp/update_status.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        status = form.save()
        return redirect('dtl_status', status.idStatus)

@method_decorator(login_required, name='dispatch')   
class StatusDeleteView(DeleteView):
    model = Status
    template_name = "monApp/delete_status.html"
    success_url = reverse_lazy('lst_status')


class ConfirmationEmailView(TemplateView):
    template_name = "monApp/email-sent.html"
    # queryset = Produit.objects.filter(id=2)
    
    def get_context_data(self, **kwargs):
        context = super(ConfirmationEmailView, self).get_context_data(**kwargs)
        context['message'] = "L'email à bien été envoyé"
        return context

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    # queryset = Produit.objects.filter(id=2)
    
    # def get_queryset(self ) :
    #     return Produit.objects.order_by("prixUnitaireProd")
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query).select_related('categorie').select_related('status')
        return Produit.objects.select_related('categorie').select_related('status')
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context

class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "ctds"
    # queryset = Categorie.objects.filter(id=2)
    
    def get_queryset(self ) :
        query = self.request.GET.get('search')
        if query:
            return Categorie.objects.filter(nomCat__icontains=query).annotate(nb_produits=Count('produits_categorie'))
        return Categorie.objects.annotate(nb_produits=Count('produits_categorie')) 
    
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
        query = self.request.GET.get('search')
        if query:
            return Status.objects.filter(libelleStatus__icontains=query).annotate(nb_produits=Count('produits_status'))
        return Status.objects.annotate(nb_produits=Count('produits_status')) 
    
    def get_context_data(self, **kwargs):
        context = super(StatusListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes status"
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"
    # queryset = Status.objects.filter(id=2)
    
    # def get_queryset(self ) :
    #     return Rayon.objects.order_by("nomRayon")
    
    def get_queryset(self):
        # Précharge tous les "contenir" de chaque rayon,
        # et en même temps le produit de chaque contenir
        query = self.request.GET.get('search')
        if query:
            return Rayon.objects.filter(nomRayon__icontains=query).prefetch_related(Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produit")))
        return Rayon.objects.prefetch_related(Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produit")))
    
    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt = []
        for rayon in context['rayons']:
            total = 0
            for contenir in rayon.contenir_rayon.all():
                total += contenir.produit.prixUnitaireProd * contenir.Qte
            ryns_dt.append({'rayon': rayon, 'total_stock': total})
        context['ryns_dt'] = ryns_dt
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
    
    def get_queryset(self):
        return Categorie.objects.annotate(nb_produits=Count('produits_categorie'))
    
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits_categorie.all()
        return context
        

class StatusDetailView(DetailView):
    model = Status
    template_name = "monApp/detail_status.html"
    context_object_name = "status"
    
    def get_queryset(self):
        return Status.objects.annotate(nb_produits=Count('produits_status'))
    
    def get_context_data(self, **kwargs):
        context = super(StatusDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du status"
        context['prdts'] = self.object.produits_status.all()
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayons"
    
    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        
        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0
        for contenir in self.object.contenir_rayon.all():
            total_produit = contenir.produit.prixUnitaireProd * contenir.Qte
            prdts_dt.append({ 'produit': contenir.produit,
                    'qte': contenir.Qte,
                    'prix_unitaire': contenir.produit.prixUnitaireProd,
                    'total_produit': total_produit} )
            total_rayon += total_produit
            total_nb_produit += contenir.Qte
            
        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit
        
        return context
        
@method_decorator(login_required, name='dispatch')   
class ContenirCreateView(CreateView):
    model = Contenir
    form_class = ContenirForm
    template_name = 'monApp/create_contenir.html'
    
    def get_context_data(self, **kwargs):
        context = super(ContenirCreateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        try:
            rayon = Rayon.objects.get(idRayon=pk)
            context['rayons'] = rayon
        except Rayon.DoesNotExist:
            raise Http404("Rayon inexistant")
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        pk = self.kwargs.get('pk')
        rayon = Rayon.objects.get(idRayon=pk)
        form.instance.rayon = rayon   
        contenir = form.save()
        return redirect('dtl_rayon', pk=pk)
    

@method_decorator(login_required, name='dispatch')
class ContenirUpdateView(UpdateView):
    model = Contenir
    form_class=ContenirForm
    template_name = "monApp/update_contenir.html"
    
    def get_object(self):
        rayon = self.kwargs.get("pk")
        produit = self.kwargs.get("pkp")
        return get_object_or_404(
            Contenir, rayon_id=rayon, produit_id=produit
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rayon = Rayon.objects.get(pk=self.kwargs.get('pk'))
        produit = Produit.objects.get(pk=self.kwargs.get('pkp'))
        context["rayon"] = rayon
        context["produit"] = produit
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        item = form.save()
        if item.Qte == 0:
            item.delete()
        return redirect('dtl_rayon', item.rayon.idRayon)

@method_decorator(login_required, name='dispatch')
class ContenirDeleteView(DeleteView):
    model = Contenir
    template_name = "monApp/delete_contenir.html"
    
    def get_success_url(self):
        return reverse_lazy("dtl_rayon", kwargs={"pk": self.kwargs.get('pk')})
    
    def get_object(self, queryset=None):
        rayon = self.kwargs.get("pk")
        produit = self.kwargs.get("pkp")
        return get_object_or_404(
            Contenir, rayon_id=rayon, produit_id=produit
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rayon"] = Rayon.objects.get(pk=self.kwargs.get('pk'))
        context["produit"] = Produit.objects.get(pk=self.kwargs.get('pkp'))
        return context
    
class ConnectView(LoginView):
    
    template_name = 'monApp/page_login.html'
    
    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
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