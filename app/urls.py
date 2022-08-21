from unicodedata import name
from xml.dom.minidom import Document
from django import conf
from django.conf import settings
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from app.models import Cart


from app import views

urlpatterns = [
    path('', views.home),
    path('productpg/', views.productpg,name='productpg'),
    # path('',views.ProductView.as_view(),name="home"),
    # path('prodview/', views.productView, name='productview'),
    
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('tracker/', views.tracker, name='tracker'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('connection/', views.connection, name='connection'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

