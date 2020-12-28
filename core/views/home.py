from django.shortcuts import render, redirect
from core.models.product import Product
from core.models.categary import Categary
from django.views import View

# Create your views here.
class Index(View):

    # cart encrease and decrease logics
    def post(self, request):
        product = request.POST['product']
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])

        return redirect('homepage')
        

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        # request.session.get['cart'].clear()
        categaries = Categary.get_all_categaries()
        CategaryID = request.GET.get('categary')
        if CategaryID:
            products = Product.get_all_product_by_categaryid(CategaryID)
        else:
            products = Product.get_all_product()
        data = {}
        data['products'] = products
        data['categaries'] = categaries
        return render(request,'index.html', data) 



# ......... about pages .........
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')