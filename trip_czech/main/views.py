from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def cs_index(request):
    return render(request, 'main/cs/index.html')
