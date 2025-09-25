from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home/home.html')
def contact(request):
    if request. method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')