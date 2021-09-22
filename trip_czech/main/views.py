from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Inquiry
from .forms import cs_FormInitial

# CZ section #


def cs_index(request):
    return render(request, 'main/cs/index.html')


def cs_services(request):
    return render(request, 'main/cs/services.html')


def cs_gallery(request):
    return render(request, 'main/cs/gallery.html')


def cs_contact(request):
    return render(request, 'main/cs/contact.html')


def cs_form_initial(request):
    if (request.method == "GET"):
        form = cs_FormInitial()
        return render(request, 'main/cs/form_init.html', {'form': form})

    if (request.method == "POST"):
        return HttpResponse("form submitted succ.")
    # DE section #


def de_index(request):
    return render(request, 'main/de/index.html')
