from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from . import models
import random,time,json

def home(request):
    products = models.Product.objects.all()
    category = models.Product_Category.objects.all()
    carousel = products.filter(id__range=(1,4))
    selling = products.filter(rating__range=(4,5)).order_by("-rating")
    contents = {
        "products":carousel,
        "categories":category,
        "selling":selling,
    }
    return render(request,"homepage.html",context=contents)

def productpage(request):

    products = models.Product.objects.all()
    product_page = products
    category = models.Product_Category.objects.all()
    brand = models.Brand.objects.all()
    pro = ""
    page = Paginator(product_page,10)
    pag_num = 1

    try:
        if "search" in request.GET:
            seacrh = request.GET['search']
            try:
                product_page = product_page.filter( Q(name__startswith=seacrh) | Q(category_id=category.get(category_name__startswith = seacrh).id))
            except ObjectDoesNotExist:
                return HttpResponse("<h1> Product, Not Found</h1>")
            
            page = Paginator(product_page,10)
        if "sort-by" in request.GET:
            pro = request.GET['sort-by']
            print(product_page)
            product_page = product_page.order_by(pro)
            page = Paginator(product_page,10)
            print(request.GET['sort-by'])

            if "filter-by" in request.GET:
                pro = request.GET['filter-by']
                cate_id = category.get(category_name = pro)
                product_page = product_page.filter(category_id = cate_id.id)
                page = Paginator(product_page,10)

        if "filter-by" in request.GET:
                pro = request.GET['filter-by']
                print(pro)
                cate_id = category.get(category_name = pro)
                product_page = product_page.filter(category_id = cate_id.id)
                page = Paginator(product_page,10)
                        
        if "page" in request.GET:
            pag_num = request.GET['page']
            product_page = page.page(pag_num)
            
        else:
            product_page = page.get_page(pag_num)
    except EmptyPage:
        product_page = page.page(page.num_pages)
        return HttpResponse("<h1> Sorry, Not Found</h1>")
    except PageNotAnInteger:
        product_page = page.page(1)
    except ObjectDoesNotExist:
        return HttpResponse("<h1> Sorry, Not Found</h1>")

    pag = page.get_elided_page_range(number=pag_num,on_each_side = 1,on_ends = 2)
    contents = {
    "products": product_page,
    "categories": category,
    "brands": brand,
    "pages": page,
    "pag_num": pag_num,
    "pags": pag,
    }
    return render(request,"products.html",context=contents)

def signuppage(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.warning(request,"password didn't match")
        else:
            try:
                user = models.User.objects.create_user(username=username,email=email,password=password)
                print(authenticate(username=username,password=password))
                custom = models.Custom_User.objects.create(user=user)
                messages.warning(request,"account created succesfully")
                return redirect("signin")
            except IntegrityError as e:
                messages.error(request,"username alrady exist")
                # storage = messages.get_messages(request)
    return render(request,"sign-up.html",{"messages":messages.get_messages(request)})

def signinpage(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request,"username or password is wrong")
    return render(request,"signin.html",{"messages":messages.get_messages(request)})

def logout_view(request):
    logout(request)
    return redirect("signin")

@login_required(login_url="/signin/")
def accountpage(request):
    context = ""
    return render(request,"AccountPage.html")

@login_required(login_url="/signin/")
def cartpage(request):
    if request.user.is_authenticated:
        cart_details,create = models.Cart_Details.objects.get_or_create(user_id=request.user.custom_user)
        cart_items = cart_details.cart_items_set.all()
    contents = {
        "details": cart_details,
        "items": cart_items
    }
    return render(request,"cart.html",context=contents)

def updatecartpage(request):
    if request.method == "POST":
        data = json.loads(request.body)
        productid = data['productid']
        action = data['action']
        user = request.user.custom_user
        product = models.Product.objects.get(id=productid)
        cart_details,create = models.Cart_Details.objects.get_or_create(user_id=user)
        cart_items,created = models.Cart_Items.objects.get_or_create(cart_id=cart_details,product_id=product)

        if action == "add":
            cart_items.quantity = (cart_items.quantity + 1)
        elif action == "remove":
            cart_items.quantity = (cart_items.quantity - 1)
        cart_items.save()
        if action == "delete" or cart_items.quantity <=0:
            cart_items.delete()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
# def searrchpage(request):

#     return render(request,"products.html")