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


class Accomodation(models.Model):
    name = models.CharField(max_length=255)
    link_to_gmaps = models.CharField(max_length=999)
    stars = models.IntegerField(default=1,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(1)
                                ])
    room_types = MultiSelectField(choices=ROOM_TYPES)


class Location(models.Model):
    name = models.CharField(max_length=255)
    part_of_republic = models.CharField(max_length=255,
                                        choices=PARTS_OF_REPUBLIC, default="CZE")


region = models.CharField(max_length=255,
                          choices=REGIONS, default="none")


class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    gdpr = models.BooleanField(default=False)
    # end of step one - COMMIT!
