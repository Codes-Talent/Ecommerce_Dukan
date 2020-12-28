from django.db import models
from .categary import Categary

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    categary = models.ForeignKey(Categary, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    # For Cart
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_product():
        return Product.objects.all()
    
    @staticmethod
    def get_all_product_by_categaryid(categary_id):
        if categary_id:
            return Product.objects.filter(categary = categary_id)
        else:
            return Product.get_all_product()