from django.shortcuts import render, get_object_or_404, redirect

from .models import Produit, Revoir

# Create your views here.

def product(request, slug):
    # product = Produit.objects.get(slug=slug) 
    product = get_object_or_404(Produit, slug=slug)

    # REVIEW for rating
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            #we GET all of this in the database
            reviews = Revoir.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first() # we get the first
                review.rating = rating
                review.content = content
                review.save()
 
            else:

                review = Revoir.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

                return redirect('product', slug=slug)
            
    
    return render(request, 'produit/produit.html', {'product': product})