from django.shortcuts import render
from django.http import HttpResponse
from login.models import User

"""
Index page of login system
"""
def index(request):
    result = {}
    password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        if login_check(email, password):
            password = "you do it"
        else:
            password = "wrong"


    return  render(request,"login/login.html", {"password" : password})






def login_check(email, password):
    user = User.objects.filter(email = email)
    if len(user) == 1 and user[0].password == password:
        return True
    else:
        return False




