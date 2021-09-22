from django.db import models
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _


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

    def __str__(self) -> str:
        return self.name + ", " + self.region

    class Meta():
        verbose_name = "Místo"
        verbose_name_plural = "Místa"


class Extra(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    region = models.CharField(max_length=3, choices=REGIONS)

    def __str__(self) -> str:
        return self.name + ", " + self.region

    class Meta():
        verbose_name = "Aktivity a ostatní"
        verbose_name_plural = "Aktivity a ostatní"


class Inquiry(models.Model):
    class Meta():
        verbose_name = "Poptávka"
        verbose_name_plural = "Poptávky"

    name = models.CharField(max_length=255, verbose_name=_('Jméno'))
    email = models.EmailField(verbose_name=_('Email'))
    gdpr = models.BooleanField(default=False, verbose_name=_('GDPR'))
    created_at = models.DateTimeField(auto_now_add=True)
    ## End of step 1 - CERATEA INQUIRY! ##
    travelling_from = models.CharField(
        max_length=5, verbose_name=_('cestuje z'), choices=COUNTRIES)

    guide_required = models.BooleanField(verbose_name=_('Chce průvodce'))
    start_date = models.DateField(verbose_name=_('Datum příjezdu'))
    end_date = models.DateField(verbose_name=_('Datum odjezdu'))
    ## End of step 2 ##
    location = models.ManyToManyField(Location)
    accomodation_type = models.CharField(
        max_length=3, choices=ACCOMODATION_TYPES)

    number_of_people = models.IntegerField(
        validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ])

    one_bed_rooms = models.IntegerField(default=0,
                                        validators=[
                                            MaxValueValidator(50),
                                            MinValueValidator(1)
                                        ])
    two_bed_rooms = models.IntegerField(default=0,
                                        validators=[
                                            MaxValueValidator(50),
                                            MinValueValidator(1)
                                        ])
    three_bed_rooms = models.IntegerField(default=0,
                                          validators=[
                                              MaxValueValidator(50),
                                              MinValueValidator(1)
                                          ])

    four_bed_rooms = models.IntegerField(default=0,
                                         validators=[
                                             MaxValueValidator(50),
                                             MinValueValidator(1)
                                         ])

    five_bed_rooms = models.IntegerField(default=0,
                                         validators=[
                                             MaxValueValidator(50),
                                             MinValueValidator(1)
                                         ])
    apartments = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(50),
                                         MinValueValidator(1)
                                     ])

    ## End of step 3 ##
    extras = models.ManyToManyField(Extra)
    note = models.TextField()

    def __str__(self) -> str:
        return self.name + ", " + self.email
