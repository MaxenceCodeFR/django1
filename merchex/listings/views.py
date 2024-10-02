from django.http import HttpResponse
from django.shortcuts import render
from .models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return HttpResponse("<h1>About</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Merci de rester en contact avec nous </p> ")