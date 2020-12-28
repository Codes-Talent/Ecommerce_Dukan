from django.views import View
from django.shortcuts import render, redirect
from core.models.customer import Customer
from core.models.product import Product
from core.models.oders import Oder
from core.middlewares.auth import auth_middleware


# ......... login pages .........
class OderView(View):

    
    def get(self, request):
        customer = request.session.get('customer')
        oders = Oder.get_oders_by_customer(customer)
        print(oders)
        return render (request, 'oders.html', {'oders':oders})