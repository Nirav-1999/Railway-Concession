from django.db import models

class StudentData(models.Model):
    student_name = models.CharField(max_length = 100)
    student_bdate = models.DateField()
    student_gender = models.CharField(max_length = 10)
    student_add1 = models.CharField(max_length = 100)
    student_add2 = models.CharField(max_length = 100)
    student_aadhar = models.IntegerField()
    student_station = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name
    