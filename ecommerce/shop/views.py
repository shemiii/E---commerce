from django.shortcuts import render
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def allprodcat(request):
    c=Category.objects.all()
    return render(request,"category.html",{'c':c})

def allproducts(request,c):
    p=Product.objects.filter(category__cname=c)
    category = Category.objects.get(cname=c)
    return render(request,"product.html",{'p':p,'category':category})
def detail(request,p):
    d=Product.objects.get(pname=p)
    return render(request,"detail.html",{'d':d})

def user_login(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allprodcat(request)
        else:
             messages.error(request,"Invalid Credentials")
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return user_login(request)

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        p1 = request.POST['p1']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if (p == p1):
            u = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            u.save()
            return user_login(request)
    return render(request,'register.html')