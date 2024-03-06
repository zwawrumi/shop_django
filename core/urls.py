from django.urls import path

from core import views as core_views
from product import views as product_views

urlpatterns = [
    path('', core_views.frontpage, name='frontpage'),
    path('signup/', core_views.signup, name='signup'),
    path('login/', core_views.loginuser, name='login'),
    path('logout/', core_views.logoutuser, name='logout'),
    path('shop/', core_views.shop, name='shop'),
    path('shop/<slug:slug>/', product_views.product, name='product'),
]