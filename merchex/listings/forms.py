from django import forms

from .models import Band, Listing


class ContactUs(forms.Form):
    """ Permet de créer un formulaire de contact """

    name = forms.CharField(label='Nom', max_length=100, required=False)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, max_length=1000, required=True)

class CreateBand(forms.ModelForm):
    class Meta:
        model = Band
        fields = "__all__"

class CreateListing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"

