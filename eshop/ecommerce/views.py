from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    slice = products[:4]
    slice1 = products[3:6]
    featuredno = products[:12]
    context = {'products': products,'slice':slice,'slice1':slice1,'featuredno':featuredno}
    template = 'index.html'
    return render(request,template,context)

#def index(request):
    #return render(request, 'index.html')

def error(request):
    return render(request, '404.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contactus(request):
    return render(request, 'contact-us.html')


def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('login')
            else:
                user=User.objects.create_user(first_name=first_name,username=username,email=email,password=password1)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password not Matching..!!')
            return redirect('login')

        return redirect('signup')
    else:
        return render(request, 'login.html')


def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request,'Username or Password is Incorrect')
            return redirect('/login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'shop.html'
    return render(request,template,context)

def productdetails(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        template = 'product-details.html'
        return render(request,template,context)
    except:
        return render(request, '404.html')

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query':q,'products':products}
        template = 'search.html'
    else:
        context = {}
        template = 'index.html'
    return render(request, template, context)
