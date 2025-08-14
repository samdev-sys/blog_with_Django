from django.shortcuts import render,HttpResponse
from django.http import HttpResponse

def bloghome(request):
    return HttpResponse("Hola desde la vista homepage")

def blogpost(request, slug):
    return HttpResponse(f"Hola desde mi  blogpost:{slug}")