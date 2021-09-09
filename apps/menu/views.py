from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allproducto = producto.objects.all()
    return render(request, 'index.html',{'allproducto':allproducto})


def contact(request):
    return render(request, 'contact.html')

def chocolate(request):
    return render(request, 'chocolate.html' )

def about(request):
    return render(request, 'about.html' )

def testimonial(request):
    return render(request, 'testimonial.html')