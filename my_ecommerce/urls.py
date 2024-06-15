from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.auth import views #=> pr log out
from django.urls import path, include

# from ecommerce.views import frontpage, boutique, signup # login_user
# from produit.views import product
# from cart.views import add_to_cart, cart, checkout

#pr une bonne pratique on a deplacé certains liens ds un fichier urls.py ds ecommerce et cart pr apres include ici
urlpatterns = [
    # path('', frontpage, name='frontpage'),
    # path('signup/', signup, name='signup'),
    # # path('login/', login_user, name='login'),
    # path('login/', views.LoginView.as_view(template_name='ecommerce/login.html'), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'), #imprter sur django
    # path('boutique/', boutique, name='boutique'),
    # path('boutique/<slug:slug>/', product, name='product'),
    path('', include('ecommerce.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('commande.urls')),
    # path('cart/', cart, name='cart'),  en deplaçant ds urls cart on a enléver les cart/
    # path('cart/checkout/', checkout, name='checkout'),
    # path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
