from django.shortcuts import render
from django.http import  HttpResponse
from listings.models import  Band
from listings.models import Listing
from django.shortcuts import  render

def hello(request):
    bands = Band.objects.all()
    return  render(request, 'listings/hello.html' ,
                   {'bands':bands})

def listings(request):
    listes = Listing.objects.all()
    return render(request, 'listes_title/listings.html', {'listes':listes})

def about(request):
    return  render(request, 'about/about.html')

def contact(request):
    return render(request, 'contact/contact.html')
