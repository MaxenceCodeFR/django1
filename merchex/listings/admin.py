from django.contrib import admin
from .models import Band, Listing

# Classe d'administration pour le modèle Band
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

# Optionnel : Vous pouvez également créer une classe d'administration pour Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('description', 'type', 'sold', 'years', 'band')

# Enregistrez chaque modèle séparément
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)  # Utilisez ListingAdmin si vous le définissez
