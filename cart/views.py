from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .cart import Cart


from produit.models import  Produit

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/partials/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html')


def update_cart(request, product_id, action):    
     #pr ajouter quantité artilce + -
     cart = Cart(request)

     if action == 'increment':
         cart.add(product_id, 1, True)

     else:
         cart.add(product_id, -1, True)
    
    # for that we need to get the Product in database
     product = Produit.objects.get(pk=product_id)
     #and i want to get the quantity of this product from the cart
     #quantity = cart.get_item(product_id)['quantity']   #get_item fonction a créé ds cart.py
     quantity = cart.get_item(product_id)

     if quantity:
        quantity = quantity['quantity']  

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price,
            },

            'total_price': (quantity * product.price) / 100,
            'quantity': quantity
            
        } 
    
     else:
         #<!-- pr supprimer par exemple on a ajouter deux articles cela ns permet de supprimer un article si on souhaite remmetre le panier a zero -->
         item = None

     response = render(request, 'cart/partials/cart_item.html', {'item': item })
     response['HX-Trigger'] = 'update-menu-cart' #end we add here this hx-trigger and update-menu..

     return response




@login_required
def checkout(request):
   #ici on met key API public 
   public_key = settings.STRIPE_API_KEY_PUBLISHABLE

   return render(request, 'cart/checkout.html', {'public_key':public_key})


def hx_menu_cart(request):
    return render(request, 'cart/partials/menu_cart.html')

def hx_cart_total(request):
    #<!-- gere total qui incremente ds summary -->
    return render(request, 'cart/partials/cart_total.html')


def paiementReussi(request):
    return render(request, 'cart/paiement_reussi.html')