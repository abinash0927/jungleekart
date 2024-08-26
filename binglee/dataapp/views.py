from django.shortcuts import render
from .models import User
from django.http import HttpResponse
import datetime


def SignUp(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        phonenumber = request.POST['telephone']
        password = request.POST['password']
        user = User(username=firstname,first_name=firstname,last_name=lastname,password=password,telephone=phonenumber,created_at=str(datetime.datetime.now().strftime('%Y-%m-%d:%H:%M:%S')))
        user.save()
    return render(request,"sign-up.html")
