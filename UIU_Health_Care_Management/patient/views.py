from django.shortcuts import render
from Users.models import *
# Create your views here.

def patient_home(request):
    # print(request.session.get('username'))
    person = Person.objects.get(username=request.session.get('username'))
    return render(request, 'patient-home.html', context={"person":person})
