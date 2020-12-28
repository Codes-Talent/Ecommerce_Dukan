from django.urls import path 
from .views import home, login, signup
from .views.login import logout
from .views.home import Index
from .views.cart import Cart
# from .views.signup import Login, Signup  OR 
from .views.checkout import CheckOut
from .views.oders import OderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('oder', auth_middleware(OderView.as_view()), name='oder'),
    path('home', Index.as_view()),
    path('about', home.about),
    path('contact', home.contact),
]