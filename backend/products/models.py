from django.db import models

from django.db.models import Q

from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.filter(lookup)
        if user is not None:
            qs = qs.filter(user=user)
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):

        return self.get_queryset().is_public().search(query, user=user)
        # return Product.objects.filter(public=True).filter(title__icontains=query)

class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True,  on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "122"
