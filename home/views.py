from django.shortcuts import render, HttpResponse
from .models import Product
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all()
    par = { 'product': products}
    pro = products
    #print(products.filter(name__iexact='lamp'))
    if request.method == "POST":
        n = request.POST.get('search')
        products = products.filter(name__icontains=n)
        if not products:
            messages.warning(request, 'Not found !')
            par = { 'product': pro}
        else:
            par = { 'product': products}
    return render(request, 'index.html', par)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent !')
    return render(request, 'contact.html')

def detail(request,mod):
    products = Product.objects.all()
    det = {}
    for i in products:
        if(i.model==mod):
            det = { 'details' : i}
    return render(request, 'detail.html',det)
