from django.shortcuts import render

# Create your views here.

def Home_view(request):
    return render(request,"home.html")

def About_view(request):
    return render(request,"about.html")

def Service_view(request):
    return render(request,"service.html")

def Gallery_view(request):
    return render(request,"gallery.html")

def Contact_view(request):
    return render(request,"contact.html")