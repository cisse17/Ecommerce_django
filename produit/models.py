from django.db import models
from django.contrib.auth.models import User

from PIL import Image
from io import BytesIO
from django.core.files import File
#1 creation de base de données produit


class Categorie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Catégories'
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description =models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
    
        # affichage prix
    def get_display_price(self):
        return self.price / 100 
    
#file image admin dashboard => au cas ou le produit n'a pa image

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url # 
        
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240.jpg'
            

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        
        return 0


class Revoir(models.Model):
    product = models.ForeignKey(Produit, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
        
