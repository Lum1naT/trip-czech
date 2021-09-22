# Generated by Django 3.1.7 on 2021-09-22 08:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('region', models.CharField(choices=[('JČ', 'Jihočeský'), ('PRG', 'Praha'), ('STŘ', 'Středočeský'), ('VYS', 'Vysočina'), ('JHM', 'Jihomoravský'), ('OLM', 'Olomoucký'), ('PAR', 'Pardubický'), ('LIB', 'Liberecký')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('part_of_republic', models.CharField(choices=[('CZE', 'Čechy'), ('MOR', 'Morava'), ('SLZ', 'Slezsko')], default='CZE', max_length=3)),
                ('region', models.CharField(choices=[('JČ', 'Jihočeský'), ('PRG', 'Praha'), ('STŘ', 'Středočeský'), ('VYS', 'Vysočina'), ('JHM', 'Jihomoravský'), ('OLM', 'Olomoucký'), ('PAR', 'Pardubický'), ('LIB', 'Liberecký')], default='none', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('gdpr', models.BooleanField(default=False)),
                ('travelling_from', models.CharField(choices=[('CZE', 'Česká Republika'), ('DEU', 'Německo'), ('AUS', 'Rakousko'), ('POL', 'Polsko'), ('SVK', 'Slovensko'), ('HUN', 'Maďarsko'), ('SWI', 'Švýcarsko'), ('ITA', 'Itálie'), ('FRA', 'Francie')], max_length=5)),
                ('guide_required', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('accomodation_type', models.CharField(choices=[('HTL', 'Hotel'), ('PNZ', 'Penzion'), ('APT', 'Apartmán')], max_length=3)),
                ('number_of_people', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('one_bed_rooms', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('two_bed_rooms', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('three_bed_rooms', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('four_bed_rooms', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('five_bed_rooms', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('apartments', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('note', models.TextField()),
                ('extras', models.ManyToManyField(to='main.Extra')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.location')),
            ],
        ),
    ]
