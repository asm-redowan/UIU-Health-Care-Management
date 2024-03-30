from django.shortcuts import render
from Users.models import *

# Create your views here.
def doctor_home(request):
    appointments = Appointment.objects.filter(status=True).order_by('appointment_date')
    person = Person.objects.get(username=request.session.get('username'))
    return render(request, 'doctor-home.html',context={"person":person, "appointments": appointments})
