from django.db import models

class CollegeData(models.Model):
    user = models.OneToOneField('accounts.CustomUser', related_name = 'college_user',on_delete=models.CASCADE)
    college_name = models.CharField(max_length = 100)
    college_location = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)


    def __str__(self):
        return self.college_name

class StudentData(models.Model):
    college = models.ForeignKey(CollegeData, on_delete=models.CASCADE)
    user = models.OneToOneField('accounts.CustomUser', related_name = 'Student_user',on_delete=models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_bdate = models.DateField()
    student_gender = models.CharField(max_length = 10)
    student_add1 = models.CharField(max_length = 100)
    student_add2 = models.CharField(max_length = 100)
    student_aadhar = models.IntegerField()
    student_station = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name
    
