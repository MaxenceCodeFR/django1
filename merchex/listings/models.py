
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Band(models.Model):

    class Genre(models.TextChoices):
        ROCK = 'R'
        POP = 'P'
        JAZZ = 'JZ'
        HIP_HOP = 'HH'
        R_AND_B = 'RB'
        COUNTRY = 'CTY'
        DANCE = 'D'
        FRENCH = 'FR'
        OTHER = 'OTHER'

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, default="N/A")
    genre = models.CharField(choices= Genre.choices ,max_length=100)
    biography = models.CharField(max_length=2000)
    year_formed = models.IntegerField(validators=[
        MinValueValidator(1900), MaxValueValidator(2024)
    ])
    active = models.BooleanField(default=True)
    official_page = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):

    class Type(models.TextChoices):

        DISK = "DISK"
        RECORD = "RECORD"
        CLOTHING = "CLOTHING"
        POSTER = "POSTER"
        MISC = "MISC"

    description = models.CharField(max_length=2000)
    sold = models.BooleanField(default=False)
    years = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2024)], null=True, blank=True)
    type = models.CharField(choices=Type.choices, max_length=100)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
