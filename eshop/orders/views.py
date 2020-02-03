from django.shortcuts import render, reverse,HttpResponseRedirect
#from carts.models import Cart
from .models import Cart,Order
import time
from .utils import id_generator
from django.contrib.auth.decorators import login_required

# Create your views here.

def orders(request):
    context = {}
    template = "checkout.html"
    return render(request, template, context)

#required user login
@login_required()
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cartview"))
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return HttpResponseRedirect(reverse("cartview"))


    if new_order.status == "Finished":
        #cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cartview"))

    context = {}
    template ="checkout.html"
    return render(request, template, context)