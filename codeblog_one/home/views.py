from django.shortcuts import render,HttpResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hola desde la vista home")
def contact(index):
    return HttpResponse("Hola desde mi  contacto")
def about(request):
    return HttpResponse("Hola desde mi about")