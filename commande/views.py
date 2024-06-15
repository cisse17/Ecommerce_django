#from django.shortcuts import render, redirect
import json
import stripe

from django.conf import settings
from django.http import JsonResponse
from.models import Commande, CommandeItem
from cart.cart import Cart

# Create your views here.  
def start_order(request):
    # recupere les infos models qu'on vient juste de creer

    cart = Cart(request)
    data = json.loads(request.body) #   ça on la mis lorsque on utilisé API ne pas oublier d'imorter json et stripe
    total_price = 0

    items = []

    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity']) 

        obj = {
            'price_data':{
                'currency': 'eur',
                'product_data': {
                    'name': product.name
                },
                
                'unit_amount': product.price,  # unit_amount qui m'avait un peu bloqué pr le paiement
            }, 
            'quantity': item['quantity']
        }

        items.append(obj) 

   
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items= items,
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/success/',
        cancel_url ='http://127.0.0.1:8000/cart/'

    )
    payment_intent = session.payment_intent


    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']
    phone = data['phone']

    order = Commande.objects.create(
        user=request.user, 
        first_name=first_name,   #je peux remplacer directement les var ici par leurs valeurs   first_name = data['first_name']
        last_name=last_name, 
        email=email, 
        phone=phone, 
        address=address, 
        zipcode=zipcode, 
        place=place,
        #payment_intent = payment_intent,
        paid_amount = total_price,
        paid = True

        )
    # order.payment_intent = payment_intent
    # order.paid_amount = total_price
    # order.paid = True
    # order.save()

    for item in cart:
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity

        item = CommandeItem.objects.create(order=order, product=product, price=price, quantity=quantity)

    #l'appel de la fonction clear ici / when the order is finiched the cart will be clear
    cart.clear() # aprés l'achat remettre le panier à 0

    return JsonResponse({'session': session, 'order': payment_intent})




#il etait comme ça au debut et on l'a modifie pr Api et ajouter data
    # if request.method == 'POST':
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('first_name')
    #     email = request.POST.get('email')
    #     address = request.POST.get('address')
    #     zipcode = request.POST.get('zipcode')
    #     place = request.POST.get('place')
    #     phone = request.POST.get('phone')

    #   for item in cart:
    #     product = item['product']
    #     quantity = int(item['quantity'])
    #     price = product.price * quantity

    #     item = CommandeItem.objects.create(order=order, product=product, price=price, quantity=quantity)


    #return redirect('moncompte')

    #return redirect('cart')


"""
    # first_name = data['first_name']
    # last_name = data['last_name']
    # email = data['email']
    # address = data['address']
    # zipcode = data['zipcode']
    # place = data['place']
    # phone = data['phone']

#ici je l'ai juste remplacer par ces valeurs commme first_name = data['first_name'], 
    order = Commande.objects.create(
        user=request.user, 
        first_name=data['first_name'], 
        last_name= data['last_name'], 
        email=data['email'], 
        phone=data['phone'], 
        address=data['address'], 
        zipcode=data['zipcode'], 
        place=data['place'],
        payment_intent = payment_intent,
        paid_amount = total_price,
        paid = True

        )"""