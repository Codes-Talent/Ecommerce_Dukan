from django.views import View
from django.shortcuts import render, redirect
from core.models.customer import Customer
from core.models.product import Product
from core.models.oders import Oder

# ......... login pages .........
class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')  #   Quantity
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            oder = Oder(customer = Customer(id=customer), product = product,
                        price = product.price,
                        address = address,
                        phone = phone,
                        quantity = cart.get(str(product.id))
                        )
            oder.placeOrder()   #   oder.save()
        request.session['cart'] = {}    

        return redirect('cart')