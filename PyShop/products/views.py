from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from . models import Other

# Create your views here.


def index(request):
    products = Product.objects.all()
    others = Other.objects.all()
    return render(request, "index.html", {"products": products, "others": others})




def new(request):
    return HttpResponse("New Products")

