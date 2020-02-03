from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('error404', views.error,name='error'),
    path('blog', views.blog,name='blog'),
    path('blogsingle', views.blogsingle,name='blogsingle'),
    #path('checkout', views.checkout,name='checkout'),
    path('contactus', views.contactus,name='contactus'),
    path('login', views.login,name='login'),
    #path('productdetails', views.productdetails,name='productdetails'),
    path('shop', views.shop,name='shop'),
    re_path(r'^shop/(?P<slug>[\w-]+)/$', views.productdetails, name='productdetails'),
    re_path(r'^s/$', views.search, name='search'),

    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('logout', views.logout, name='logout'),

]
