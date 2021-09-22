from django.db import models
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator


ROOM_TYPES = (
    ('1', 'Jednolůžkový'),
    ('2', 'Dvojlůžkový'),
    ('3', 'Trojlůžkový'),
    ('4', 'Čtyřlůžkový'),
)


ACCOMODATION_TYPES = (
    ('HTL', 'Hotel'),
    ('PNZ', 'Penzion'),
    ('APT', 'Apartmán'),
)

PARTS_OF_REPUBLIC = (
    ('CZE', 'Čechy'),
    ('MOR', 'Morava'),
    ('SLZ', 'Slezsko'),
)

REGIONS = (
    ('JČ', 'Jihočeský'),
    ('PRG', 'Praha'),
    ('STŘ', 'Středočeský'),
    ('VYS', 'Vysočina'),
    ('JHM', 'Jihomoravský'),
    ('OLM', 'Olomoucký'),
    ('PAR', 'Pardubický'),
    ('LIB', 'Liberecký'),
)


COUNTRIES = (
    ('CZE', 'Česká Republika'),
    ('DEU', 'Německo'),
    ('AUS', 'Rakousko'),
    ('POL', 'Polsko'),
    ('SVK', 'Slovensko'),
    ('HUN', 'Maďarsko'),
    ('SWI', 'Švýcarsko'),
    ('ITA', 'Itálie'),
    ('FRA', 'Francie'),

)

'''
class Accomodation(models.Model):
    name = models.CharField(max_length=255)
    link_to_gmaps = models.CharField(max_length=999)
    stars = models.IntegerField(default=1,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(1)
                                ])
    room_types = MultiSelectField(choices=ROOM_TYPES)

'''


class Location(models.Model):
    name = models.CharField(max_length=255)
    part_of_republic = models.CharField(max_length=3,
                                        choices=PARTS_OF_REPUBLIC, default="CZE")

    region = models.CharField(max_length=3,
                              choices=REGIONS, default="none")


class Extra(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=3, choices=REGIONS)


class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    gdpr = models.BooleanField(default=False)
    ## End of step 1 - CERATEA INQUIRY! ##
    travelling_from = models.CharField(max_length=5, choices=COUNTRIES)
    guide_required = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    ## End of step 2 ##
    location = models.ForeignKey(Location,
                                 on_delete=models.SET_NULL, null=True)
    accomodation_type = models.CharField(
        max_length=3, choices=ACCOMODATION_TYPES)
    number_of_people = models.IntegerField(
        validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ])

    ## End of step 3 ##
    extras = models.ManyToManyField(Extra)
    note = models.TextField()
