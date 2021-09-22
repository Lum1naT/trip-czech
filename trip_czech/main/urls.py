"""trip_czech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from . import views

urlpatterns = [
    # CZ section - include both cs/ and '' versions! two per page!
    path('cs/', views.cs_index, name="cs_index"),
    path('', views.cs_index, name="cs_index"),
    path('cs/galerie', views.cs_gallery, name="cs_gallery"),
    path('galerie', views.cs_gallery, name="cs_gallery"),
    path('cs/sluzby', views.cs_services, name="cs_services"),
    path('sluzby', views.cs_services, name="cs_services"),
    path('cs/kontakt', views.cs_contact, name="cs_contact"),
    path('kontakt', views.cs_contact, name="cs_contact"),
    path('cs/poptavka/1', views.cs_form_initial, name="cs_form_initial"),



    # DE section
    path('de/', views.de_index, name="de_index"),


]
