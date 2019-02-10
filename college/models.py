<<<<<<< HEAD
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser

class CollegeData(models.Model):
    user = models.OneToOneField('accounts.CustomUser', related_name = 'college_user',on_delete=models.CASCADE, blank = True)
    college_name = models.CharField(max_length = 100)
    college_location = models.CharField(max_length = 100)
    


    def __str__(self):
        return self.college_name

class StudentData(models.Model):
    college = models.ForeignKey(CollegeData, on_delete=models.CASCADE, blank = True)
    user = models.OneToOneField('accounts.CustomUser', related_name = 'Student_user',on_delete=models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_bdate = models.DateField()
    student_gender = models.CharField(max_length = 10)
    student_add1 = models.CharField(max_length = 300)
    student_add2 = models.CharField(max_length = 300)
    student_aadhar = models.IntegerField()
    student_station = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name
    

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_student:
		StudentData.objects.get_or_create(user = instance)
	else:
		CollegeData.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_student:
		instance.Student_user.save()
	else:
=======
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser

class CollegeData(models.Model):
    user = models.OneToOneField('accounts.CustomUser', related_name = 'college_user',on_delete=models.CASCADE, blank = True)
    college_name = models.CharField(max_length = 100)
    college_location = models.CharField(max_length = 100)
    


    def __str__(self):
        return self.college_name

class StudentData(models.Model):
    college = models.ForeignKey(CollegeData, on_delete=models.CASCADE, blank = True)
    user = models.OneToOneField('accounts.CustomUser', related_name = 'Student_user',on_delete=models.CASCADE)
    student_bdate = models.DateField()
    student_gender = models.CharField(max_length = 10)
    student_add1 = models.CharField(max_length = 300)
    student_add2 = models.CharField(max_length = 300)
    student_aadhar = models.IntegerField()
    student_station = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name
    

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_student:
		StudentData.objects.get_or_create(user = instance)
	else:
		CollegeData.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_student:
		instance.Student_user.save()
	else:
>>>>>>> 8839679c1e81b73ed1a1b9da787586e8dc2fcb01
		CollegeData.objects.get_or_create(user = instance)