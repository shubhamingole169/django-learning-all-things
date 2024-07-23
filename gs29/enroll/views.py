
from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    

    # fm = StudentRegistration(auto_id='some_%s')  # IDs will have a prefix 'some_'
    # fm = StudentRegistration(auto_id=True)       # IDs will be automatically generated (default behavior)
    # fm = StudentRegistration(auto_id=False)      # No IDs will be generated

    fm = StudentRegistration(auto_id=True, label_suffix=' ', initial={'name': 'Sonam' , 'email':'sonam@fmail.com' })  # Automatically generate IDs, no label suffix

    return render(request, 'enroll/userregistration.html', {'form': fm})
