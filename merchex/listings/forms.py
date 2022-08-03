from django import forms

from listings.models import Band, Listing

# Création d'un formulaire à partir de zéro
class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

# Création d'un formulaire à partir d'un modèle existant
class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # Sélection de tous les champs du modèle
        #fields ='__all__'
        # Sélection de tous les champs sauf
        exclude = ('active', 'official_homepage')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # Sélection de tous les champs
        fields = '__all__'
