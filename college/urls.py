from django.conf.urls import url
from . import views

app_name = 'college'

urlpatterns = [
    url(r'^college-sign-up/$',views.college_signup_view, name='College-SignUp'),
    url(r'^add-student/$',views.add_student, name='Add-Student'),
    url(r'^college-login/$',views.login_page, name='login'),
    url(r'^college/$',views.StudentDetailView.as_view(), name='dashboard'),
    url(r'^$',views.LandingView,name = "landing"),
   

]