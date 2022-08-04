from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)  # Récupérer le band avec cet id
    return render(request, 'listings/band_detail.html',
                  {'band': band})  # Pour passer le groupe au gabarit


def band_create(request):
    #print("Methode",request.method)
    #print("Post",request.POST)
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            #Créer une nouvelle bande et la stocker dans db
            band = form.save()
            # Redirige vers la page bande-detail que nous avons créer
            return  redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html',
                  {'form':form})

def band_change(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST,instance=band)
        if form.is_valid():
            # Mettre à jour le groupe existant
            form.save()
            # Rédiriger vers la page detail
            return redirect('band-detail',band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_change.html',
                  {'form':form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        # Supprimer le modèle
        band.delete()
        # Rédiriger vers la band-list
        return redirect('band-list')
    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'listings/band_delete.html',
                  {'band':band})


def listings(request):
    listes = Listing.objects.all()
    return render(request, 'listes_title/listing_list.html',
                  {'listes': listes})


def listing_detail(request, id):
    listes_det = Listing.objects.get(id=id)  # Pour obtenir la liste avec l'id
    return render(request, 'listes_title/listing_detail.html',
                  {'listes_det': listes_det})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid:
            liste = form.save()
            return redirect('listing-detail', liste.id)
    else:
        form = ListingForm()
    return render(request, 'listes_title/listing_create.html',
                  {'form':form})

def listing_change(request, id):
    # Récupération de la liste d'objets
    liste = Listing.objects.get(id=id)
    #Vérification si la réquête est un post et que le formulaire est valide
    if request.method == 'POST':
        form = ListingForm(request.POST,instance=liste)
        if form.is_valid:
            form.save()
            return redirect('listing-detail', liste.id)
    else:
        form = ListingForm(instance=liste)
    return render(request, 'listes_title/listing_change.html',
                  {'form':form})

def listing_delete(request,id):
    liste = Listing.objects.get(id=id)
    if request.method == 'POST':
        #Supprimer la l'annonce
        liste.delete()
        # Rédiriger vers la liste d'annonces
        return redirect('listing-list')
    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'listes_title/listing_delete.html',
                  {'liste':liste})



def about(request):
    return render(request, 'about/about.html')


def contact(request):
    # Les déclaration de journalisation pour voir ce qui est rétourner dans le terminal en fonction des requêtes
    # print("La méthode requête est : ", request.method)
    # print("La méthode Post est : ", request.POST)

    if request.method == 'POST':
        # Créer une instance du formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']

                # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
                # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
            )
            return redirect('email-sent')
    else:
        # Ceci doit être une réquête GET donc laisser le formulaire vide
        # Instance de la classe ContactUsForm
        form = ContactUsForm()

    # form = ContactUsForm() # Ajout d'un nouveau formulaire
    return render(request, 'contact/contact.html',
                  {'form': form})  # Passe ce formulaire au gabarit


def email_sent(request):
    return render(request, 'contact/email_sent.html')
