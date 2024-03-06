from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from product.models import Product, Category

from .forms import SignUpForm

def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
        else:
            print(form.errors)
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

@csrf_protect
def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'GET':
        return render(request, 'core/login.html', {'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'core/login.html', {
                'form': form,
                'error': 'Username or password did not match'
                })
        else:
            login(request, user)
            return redirect('frontpage')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('frontpage')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'core/shop.html', context)


#### LOGOUTUUUUTU