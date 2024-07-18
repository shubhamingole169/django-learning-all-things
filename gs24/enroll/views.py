from django.shortcuts import render
from enroll.models import Student
# from .models import Student

# Create your views here.

def studentinfo(request):
    stud = Student.objects.all() # this will return all data present
    
    # stud = Student.objects.get(pk=2)  # this will return single data
    
    # print('myoutput',stud)
    return render(request, 'enroll/studeatils.html',{'stu':stud})
