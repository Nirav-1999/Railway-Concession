from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentData,CollegeData
# from .forms import CollegeSignUpForm
# Register your models here.
# class CollegeAdmin(admin.ModelAdmin):
#     add_form = CollegeSignUpForm
#     form = CollegeSignUpForm
#     list_display = ['college_name']


admin.site.register(CollegeData)
admin.site.register(StudentData)