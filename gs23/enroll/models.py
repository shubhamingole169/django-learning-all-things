from django.db import models

# Create your models here.

class Student(models.Model):
    stuid = models.IntegerField()
    # stuid = models.ImageField(primary_key=true)  # this will make its primary key
    stuname = models.CharField(max_length= 70)
    stuemail = models.EmailField(max_length=70)
    # stuemail2 = models.EmailField(max_length=70 , default='not neccesssary')
    stupass = models.CharField(max_length=70)
    
