
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Contact, Customer, OrderUpdate, Orders, Product, Cart, OrderPlaced, Productpg
# from requests
from math import ceil
from django.views.generic import ListView
from django.http import HttpResponse


# API_KEY = '97154f0cb0fc4589b098a65ac9fa32d6'




def home(request):
    
  

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allProds}

    # url = f'https://newsapi.org/v2/everything?q=tesla&from=2022-04-05&sortBy=publishedAt&apiKey=97154f0cb0fc4589b098a65ac9fa32d6'
   
    # response = requests.get(url)
    # data = response.json()

    # results = data['results']

    # context = {
    #     'results': results
    # }
    return render(request, 'app/home.html', params)


def productpg(request):
    
  

    allProds = []
    catprods = Productpg.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Productpg.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allProds}

    # url = f'https://newsapi.org/v2/everything?q=tesla&from=2022-04-05&sortBy=publishedAt&apiKey=97154f0cb0fc4589b098a65ac9fa32d6'
   
    # response = requests.get(url)
    # data = response.json()

    # results = data['results']

    # context = {
    #     'results': results
    # }
    return render(request, 'app/productpg.html', params)    

# def productView(request, myid):
#     product = Product.objects.filter(id=myid)


# # def add_to_cart(request):
    
# #     return render(request, 'app/addtocart.html')

def add_to_cart(request):
 return render(request, 'app/cart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')






def about(request):
    return render(request, 'app/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'app/contact.html')

def connection(request):
    return render(request, 'app/connection.html')
           

def login(request):
    return render(request, 'app/login.html')


def customerregistration(request):
    return render(request, 'app/customerregistration.html')


def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'app/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'app/checkout.html')
def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "app/prodView.html", {'product':product[0]})    


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'app/tracker.html')
def search(request):
    return render(request, 'app/search.html')