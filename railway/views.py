from django.shortcuts import render
from accounts.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import  AuthenticationForm


def RailwayLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        print(form)
        # print(form)
        if form.is_valid():
            print("----HI----")
            user = form.get_user()
            print(user)
            login(request, user)    
            if user.is_railway:
                return render(request, "railway/table2.html", {"form" : form} )
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
        return render(request, "railway/railway.html", {"form":form})