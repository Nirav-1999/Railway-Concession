from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser
from django import forms
from django.db import transaction
from .models import CollegeData,StudentData

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', )
 
class CollegeDataForm(forms.ModelForm):
    class Meta:
        model = CollegeData
        fields = ('college_name', 'college_location')
        
class StudentDataForm(forms.ModelForm):
    class Meta:
        model = StudentData
        exclude = ('college',)
        fields = ('college','student_gender','student_add1','student_add2','student_aadhar','student_station')
