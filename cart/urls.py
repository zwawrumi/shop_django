from django.urls import path

from cart import views as cart_views

urlpatterns = [
    path('add_to_cart/<int:product_id>/', cart_views.add_to_cart, name='add_to_cart'),    
    path('', cart_views.cart, name='cart'),
    path('checkout/', cart_views.checkout, name='checkout')
]