from django.shortcuts import render, redirect
from datetime import datetime
from Users.models import *
from django.db.models import F, Window
from django.db.models.functions import RowNumber
# Create your views here.

def patient_home(request):
    # print(request.session.get('username'))
    appointments = Appointment.objects.filter(status=True).order_by('appointment_date')
    c = 0
    appointment = None
    rank = None
    for a in appointments:
        c = c + 1
        if a.patient.username == request.session.get('username'):
            appointment = a
            rank =  c
            break
    
   
    person = Person.objects.get(username=request.session.get('username'))
    return render(request, 'patient-home.html', context={"person":person, "rank": rank, "appointment": appointment})


def take_appointment(request):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if request.method == "POST":
        time =  request.POST['time']
        problem  = request.POST['problem']
        username = request.session.get('username')

        dic = {'patient': username, 'appointment_date': dt_string, 'status': True, 'slot':time, 'problem': problem}

        try:

            if not Appointment.objects.filter(patient=username).exists():
                patient = Person.objects.get(username=username)
                Appointment.objects.create(patient=patient,problem=problem,slot=time,status=True,appointment_date=timezone.now())
                # appointment = Appointment.objects.create(dic)
                return redirect('patient-home')
            else:
                appointment = Appointment.objects.get(patient=username)
                appointment.date_time = dt_string
                appointment.problem = problem
                appointment.status = True
                appointment.save()
                return redirect('patient-home')
            
        except Appointment.DoesNotExist:
            pass
        
    return render(request,'take-appointment.html')