from django.shortcuts import render,HttpResponse
from django.http import HttpResponse

def bloghome(request):
    return render(request,'blog/bloghome.html')

def blogpost(request, slug):
    return render(request,'blog/blogpost.html')