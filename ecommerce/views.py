from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q # pr la barre de recherche
# Create your views here.
from produit.models import Produit, Categorie
from .form import SignUpForm

def frontpage(request):
    products =Produit.objects.all()[0:8] # if you want to get 8 'first produit' from the database use slice in python
    return render(request, 'ecommerce/frontpage.html', {'products':products})

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'ecommerce/signup.html', {'form': form })


# def login_user(request):
#     return render(request, 'ecommerce/login.html')

@login_required
def monCompte(request):
    return render(request, 'ecommerce/moncompte.html')


@login_required
def editerMonCompte(request):
    # pr editer le compte je recupere les nouvelles infos
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        #1ere chose faite on a juste par las var par leurs valeurs au dessus
        # if request.method == 'POST':
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # username = request.POST.get('username')
        # email = request.POST.get('email')

        # user = request.user
        # user.first_name = first_name
        # user.last_name = last_name
        # user.email = email
        # user.username = username
        # user.save()

        return redirect('moncompte')

    return render(request, 'ecommerce/editer_moncompte.html')


def boutique(request):
    categories = Categorie.objects.all()
    products =Produit.objects.all() # if you want to get 8 'first produit' from the database
    
    active_categorie = request.GET.get('categorie', '') # la categorie active pr ns permettre de savoir on est ds quelle categorie quand on clique sur une des cateories
    
    if active_categorie:
        products = products.filter(categorie__slug=active_categorie) # pr filtrer nos categories

    query = request.GET.get('query', '')

    if query:
      products = products.filter(Q(name__icontains=query) | Q(description__icontains=query)) #on met le Q si on veut par exemple la recercher se fasse aussi par la description
    
    context = {
        'categories': categories,
        'products':products,
        'active_categorie': active_categorie
    }
    return render(request, 'ecommerce/boutique.html', context)


def apropos(request):
    return render(request, 'ecommerce/apropos.html')