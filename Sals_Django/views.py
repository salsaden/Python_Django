from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def AboutUs(request):
    return render(request,"About Us.html")