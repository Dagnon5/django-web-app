from django.contrib import admin
from listings.models import Band
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name','year_formed','genre') # Liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # Nous modifions cette ligne en ajoutant un deuxième argument

# Création de la classe ListingAdmin pour le modèle Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','type','year','band')
# Affichage de listing sur la page d'administration
admin.site.register(Listing,ListingAdmin)