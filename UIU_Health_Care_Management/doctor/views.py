from django.shortcuts import render, redirect
from django.http import HttpResponse
from Users.models import *

# Create your views here.
def doctor_home(request):
    appointments = Appointment.objects.filter(status=True).order_by('appointment_date')
    # appointments = Appointment.objects.all()

    # print(appointments)

    person = Person.objects.get(username=request.session.get('username'))
    return render(request, 'doctor-home.html',context={"person":person, "appointments": appointments})


def patientprofile(request, username):
    patient = Person.objects.filter(username=username)
    if patient.exists():
        return HttpResponse("patient")
    else:
        return redirect("doctor-home")
    
    
