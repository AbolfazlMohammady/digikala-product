from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
 
from django.contrib import messages

from .models import Product, Category
from .forms import SingUpForm

def homeview(request):

    all_products = Product.objects.all()

    return render(request, 'index.html' , {'products': all_products})

def aboutview(request):
    return render(request, 'about.html' )

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            messages.success(request, ('با موفقیت وارد شدید!'))
            return redirect('home')
        else:
            # Display an error message
            error_message = "Invalid credentials"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Display the login form
        return render(request, 'login.html')

def logout_user(request):
   logout(request)
   messages.success(request, ('با موفقیت خارج شدید!'))
   return redirect('home')

def singup_user(request):
    form = SingUpForm()
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, ('با موفقیت ثبت نام شدید!'))
            return redirect('home')
        else:
            messages.success(request, ('مشکلی در ثبت نام وجود دارد'))
            return redirect('singup')

    else:
      return render(request, 'singup.html', {'form':form})
   

def product(request,pk):
    product = Product.objects.get(id= pk)
    return render(request, 'product.html' , {'product': product})


def category(request,cat):
    cat = cat.replace('-' ,' ')
    try:
        category = Category.objects.get(name=cat)
        product = Product.objects.filter(category=category)
        return render(request, 'category.html' , {'product': product, 'category': category} )  
    except:
        messages.success(request,('دسته بندی وجود ندارد'))
        return redirect('home')