from django.contrib import admin

# Register your models here.
from .models import Categorie, Produit

admin.site.register(Categorie)
admin.site.register(Produit)