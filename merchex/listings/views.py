from typing import List

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Band, Listing
from .forms import ContactUs, CreateBand, CreateListing
from django.core.mail import send_mail


def band_list(request):
    """Renvoi un template pour afficher la liste des groupes"""
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):

    """Renvoi un template pour afficher le detail d'un groupe"""

    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_update(request, id):
    """Créer un template de formulaire pour modifier un groupe"""
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = CreateBand(request.POST, instance=band)
        if form.is_valid():

            form.save()

            return redirect('band_detail', band.id)

    form = CreateBand(instance=band)
    return render(request, 'listings/band_update.html', {'form': form, 'band': band})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band_list')

    return render(request, 'listings/band_delete.html', {'band': band})

def list_list(request):
    lists = Listing.objects.all()
    return render(request, 'listings/list_list.html', {'lists': lists})

def list_detail(request, id):
    list = Listing.objects.get(id=id)
    return render(request, 'listings/list_detail.html', {'list': list})

def list_create(request):
    if request.method == 'POST':
        form = CreateListing(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_list')
    else:
        form = CreateListing()

    return render(request, 'listings/list_create.html', {'form': form})

def list_update(request, id):
    list = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = CreateListing(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('list_list')
    else:
        form = CreateListing(instance=list)
        return render(request, 'listings/list_update.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)

        if form.is_valid():
            send_mail(
                subject= f"Message from {form.cleaned_data['name'] or 'anonyme'} via Merchex",
                message = form.cleaned_data['message'],
                from_email = form.cleaned_data['email'],
                recipient_list = ['admin@merchex.xyz'],
            )
        return redirect('email-sent')
    else:
        form = ContactUs()
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    return render(request, 'listings/contact_us.html', {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def band_create(request):
    if request.method == 'POST':
        form =  CreateBand(request.POST)

        if form.is_valid():
            band = form.save()

            return redirect('band_detail', band.id)
    else:
        form = CreateBand()
    return render(request, 'listings/band_add.html', {'form': form})

def about(request):
    return HttpResponse("<h1>About</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Merci de rester en contact avec nous </p> ")