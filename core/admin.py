from django.contrib import admin
from .models.product import Product
from .models.categary import Categary
from .models.customer import Customer
from .models.oders import Oder

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'categary']

class AdminCategary(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile', 'email', 'password']

    
# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Categary, AdminCategary)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Oder)
