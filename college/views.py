from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from accounts.models import CustomUser
from django.contrib.auth.forms import  AuthenticationForm
from .forms import CollegeDataForm,UserForm,StudentDataForm
from .models import CollegeData,StudentData
from django.views import generic
from django.shortcuts import get_object_or_404


def college_signup_view(request):
    user_form = {}
    profile_form ={}
    
    if request.method == 'POST':
		
        user_form = UserForm(request.POST)
        profile_form = CollegeDataForm(request.POST)
        print(user_form)
            
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_college = True
            user.save()

            user.college_user.college_name = profile_form.cleaned_data.get('college_name')
            user.college_user.college_location = profile_form.cleaned_data.get('college_location')
            user.college_user.save()
            return redirect('college:login')
        else:
            print(user_form.errors)
            user_form = UserForm(prefix='UF')
            profile_form = CollegeDataForm(prefix='PF')
            
    return render(request, 'college/register.html',{
                'user_form': user_form,
                'profile_form': profile_form,
            })

def add_student(request):
    user_form = {}
    profile_form ={}
    
    if request.method == 'POST':
        profile_form = StudentDataForm(request.POST)
            
        if profile_form.is_valid():
            college = request.user
            a = CustomUser.objects.get(username = college)
            
            # import pdb; pdb.set_trace()
            # print(college)
            profile_form=profile_form.save(commit = False)
            profile_form.college = a.college_user
            

            profile_form.save()
            return redirect('college:dashboard')
        else:
            print(profile_form.errors)
            user_form = UserForm()
            profile_form = CollegeDataForm()
            
    return render(request, 'college/details.html',{
                'user_form': user_form,
                'profile_form': profile_form,
            })

def login_page(request):
    if request.method == "POST":
        if request.POST['type'] == 'A':
            aadhar = request.POST['Aadhar_no']
            college = request.POST['college']
            a = StudentData.objects.get(student_aadhar = aadhar)
            return render(request,'college/studentdetails.html',{'student':a})

        else:
            form = AuthenticationForm(data = request.POST)
            print(form)
            # print(form)
            if form.is_valid():
                user = form.get_user()
                login(request, user)    
                return redirect('college:dashboard')
            else:
                print(form.errors)
        


    else:
        form = AuthenticationForm()
        return render(request, "college/index.html", {"form" : form})
    

class StudentDetailView(generic.ListView):
    model=StudentData
    template_name='college/table.html'
    context_object_name='students'
    def get_queryset(self):
        return StudentData.objects.all()

def LandingView(request):
    return render(request,'college/landing.html')   

<<<<<<< HEAD
=======

>>>>>>> c3f39a9771eb7ac3218cac82de157f4a9f099388
