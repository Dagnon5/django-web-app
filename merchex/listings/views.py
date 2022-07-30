from django.shortcuts import render
from django.http import  HttpResponse
from listings.models import  Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return  render(request, 'listings/band_list.html' ,
                   {'bands':bands})
def band_detail(request,id):
    band = Band.objects.get(id=id) # Récupérer le band avec cet id
    return render(request, 'listings/band_detail.html',
                  {'band':band}) # Pour passer le groupe au gabarit

def listings(request):
    listes = Listing.objects.all()
    return render(request, 'listes_title/listings.html', {'listes':listes})


def listing_detail(request, id):
    #listes_det = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html',
                   {'id':id})


def about(request):
    return  render(request, 'about/about.html')

def contact(request):
    return render(request, 'contact/contact.html')
