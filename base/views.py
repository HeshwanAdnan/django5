from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse("Hi i am Heshwan from university of sulaimani")
