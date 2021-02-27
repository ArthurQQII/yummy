from django.shortcuts import render

# Create your views here.
def index(request):
    views_name = "hello woxxxrd"
    return  render(request,"login/login.html", {"name":views_name})