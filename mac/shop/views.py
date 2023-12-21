from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    obj = Product.objects.all()
    return render(request,'index.html',{'obj':obj})

def about(request):
    return render(request,"about.html") 

def contact(request):
    return render(request,"contact.html")

def tracker(request):
    return render(request,"tracker.html")

def search(request):
    return render(request,"search.html")

def ProductView(request):
    return render(request,"ProductView.html")

def checkout(request):
    return render(request,"checkout.html")