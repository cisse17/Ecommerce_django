from django.contrib.auth.models import User
from django.db import models
from produit.models import Produit

# Create your models here.
#creation d'une nouvelle base de données pr les commandes

class Commande(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        ( ORDERED, 'ordered'),
        ( SHIPPED, 'shipped'),

    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)


    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ('-created_at',) #like this I new one item 'in mes commandes=> front' will be in the top

    def get_total_price(self): #total general ds mes commande 
        if self.paid_amount:
            return self.paid_amount / 100
        
        return 0
    

class CommandeItem(models.Model):
    order = models.ForeignKey(Commande, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product


    # fonction pr afficher total price dans mes mon compte => commandes prix afficher en haut a droit
    def get_total_price(self):
        return self.price  / 100

