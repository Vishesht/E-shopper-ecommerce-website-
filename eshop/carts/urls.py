from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.cartview,name='cartview'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.update_cart, name='update_cart'),
]