from django.shortcuts import render
from accounts.models import CustomUser

def RailwayLogin(request):
    if request.method == "POST":
        uname = request.POST["username"]
        passw = request.POST["LGform2_pwd"]
        obj = CustomUser.objects.get('username' == uname)
        if obj.password == passw:
            return 

    else:
        pass
    return render(request,'railway/railway.html')
