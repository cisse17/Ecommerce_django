from .cart import Cart



def cart(request):
    return {'cart': Cart(request)}

#aprés on a ajouté ce fichie ou dict dans notre fichiers settings partie template 