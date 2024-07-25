
from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
            # print(fm)
        if fm.is_valid():
            print("form validated")
            print("this is from post method")
            # name = request.POST['name']           # this is also work but this is bad practice !!
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            
            print("name :",name)
            print("email :",email)
            print("password :", password)
            # fm = StudentRegistration()     # this is bad practice it can be reenter data
    else:
        fm = StudentRegistration()
        print("this is from get request")

    return render(request, 'enroll/userregistration.html', {'form': fm})
