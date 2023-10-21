from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Some stupid shit index")

# Create your views here.
