from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import  AuthenticationForm
from django.views import generic
from college.models import CollegeData,StudentData

def RailwayLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        print(form)
        print()
        # print(form)
        if form.is_valid():
            print("----HI----")
            user = form.get_user()
            print(user)
            login(request, user)   
            if user.is_railway:
                print("valid") 
                return redirect('railway:table')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
        return render(request, "railway/railway.html", {"form":form})

class StudentDetailView(generic.ListView):
    model=StudentData
    template_name='railway/table2.html'
    context_object_name='students'
    def get_queryset(self):
        return StudentData.objects.all()

def ticketview(request,pk):
    data = StudentData.objects.get(pk=pk)
    print("------------------")
    print(data)
    return render(request,'railway/ticket.html',{'student':data})