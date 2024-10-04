"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    # ADMIN URLS
    path('admin/', admin.site.urls),

    # BAND URLS
    path('bands/', views.band_list, name='band_list'),
    path('bands/<int:id>/', views.band_detail, name='band_detail'),
    path('bands/add/', views.band_create, name='band_create'),

    # MERCH URLS
    path('listings/', views.list_list, name='list_list'),
    path('listings/<int:id>/', views.list_detail, name='list_detail'),
    path('listings/add/', views.list_create, name='list_create'),

    # MISC URLS
    path('contact-us/', views.contact_us, name='contact_us'),
    path('thank-you/', views.email_sent, name='email-sent'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
