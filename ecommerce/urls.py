from django.urls import path
from django.contrib.auth import views #=> pr log out

from ecommerce.views import frontpage, boutique, signup, monCompte, editerMonCompte, apropos # login_user
from produit.views import product

urlpatterns = [
    
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    # path('login/', login_user, name='login'),
    path('login/', views.LoginView.as_view(template_name='ecommerce/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'), #imprter sur django
    path('moncompte/', monCompte, name='moncompte'),
    path('moncompte/editer/', editerMonCompte, name='editer_moncompte'),
    path('boutique/', boutique, name='boutique'),
    path('boutique/<slug:slug>/', product, name='product'),
    path('apropos', apropos, name='apropos'),
]


#pr une bonne pratique on a deplacé certains liens ds un fichier urls.py ds ecommerce et cart pr apres include ici
