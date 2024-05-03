from django.shortcuts import render, redirect
from django.http import HttpResponse
from Users.models import *
from .models import *
from dateutil.relativedelta import relativedelta
import datetime
from django.urls import reverse
# Create your views here.
def doctor_home(request):
    if not request.session.get('username'):
        return redirect('index')
    appointments = Appointment.objects.filter(status=True).order_by('appointment_date')
    # appointments = Appointment.objects.all()

    # print(appointments)

    person = Person.objects.get(username=request.session.get('username'))
    return render(request, 'doctor-home.html',context={"person":person, "appointments": appointments})


def patientprofile(request, username):
    if not request.session.get('username'):
        return redirect('index')
    
    appointment = Appointment.objects.get(patient=username)
    appointment.status = False
    appointment.save()

    patient = Person.objects.filter(username=username)
    pat= patient.first()
    prescription = Prescription.objects.filter(patient=pat).order_by('id')

    print(pat.username)
    if patient.exists():
        return render(request, 'patient-profile.html', context={"patient": pat,"prescriptions":prescription})
        # return HttpResponse(patient)
    
    else:
        return redirect("doctor-home")
    
def addprescription(request, username):
    if not request.session.get('username'):
        return redirect('index')
    patient = Person.objects.filter(username=username);
    patient = patient.first()

    

    birthdate_str = patient.dob.strftime('%Y-%m-%d') # Example birthdate in the format YYYY-MM-DD
    birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    today = datetime.date.today()
    age = relativedelta(today, birthdate).years

    # print("Your age is", age, "years.")
    doctor = Person.objects.get(username=request.session.get('username'))


    # print(patient.dob)
    return render(request, 'add_prescription.html', context={"patient": patient, 'age':age, "doctor": doctor})

def viewprescription(request, prescription_id):
    if not request.session.get('username'):
        return redirect('index')
    prescription = Prescription.objects.get(id=prescription_id)
    print(prescription.patient.first_name)
    symptoms_list = prescription.symptoms.split('\r\n')
    medicine_list = prescription.drug.split('\r\n')
    test_list = prescription.test.split('\r\n')
    diagnosis_list = prescription.diagnosis.split('\r\n')
    # print(symptoms_list)
    return render(request, 'viewprescription.html', context={"prescription": prescription, 'symptoms_list': symptoms_list, 'medicine_list': medicine_list,'test_list':test_list,'diagnosis_list':diagnosis_list})
    # return HttpResponse(prescription_id)

def save(request):
    if not request.session.get('username'):
        return redirect('index')

    if request.method == 'POST':
        doctor = request.POST['doctor']  # Retrieve the submitted data
        # doctor = request.POST.copy().get('doctor')  # Retrieve the submitted data
        patient = request.POST['patient']  # Retrieve the submitted data
        diagnosis = request.POST['diagnosis']  # Retrieve the submitted data
        symptoms = request.POST['symptoms']  # Retrieve the submitted data
        medicine = request.POST['medicine']  # Retrieve the submitted data
        test = request.POST['test']  # Retrieve the submitted data
        pat = Person.objects.get(username=patient)
        doc = Person.objects.get(username=doctor)
        print(doctor, patient, diagnosis, medicine, test)
        # symptoms_list = symptoms.split('\r\n')
        # print(symptoms_list)
        prescription = Prescription.objects.create(patient=pat,doctor=doc,symptoms=symptoms,diagnosis=diagnosis,drug=medicine,test=test)
        prescription.save()
        pres= Prescription.objects.filter(patient=pat).order_by('id')
        # return HttpResponse(f'Hello, {doctor, patient,symptoms, diagnosis, medicine, test}! Form submitted successfully.')
        # return render(request, 'patient-profile.html', context={"patient": pat,"prescriptions":prescription})
        redirect_url = reverse('patientprofile', kwargs={'username': patient})
        # return redirect("patientprofile")
        return redirect(redirect_url)
    

def nearesthospital(request):
    return render(request,'nearesthospital.html')


def search(request):
    if not request.session.get('username'):
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        print(username)

        person = Person.objects.filter(username=username).first()

    if person:
        redirect_url = reverse('patientprofile', kwargs={'username': person.username})
        return redirect(redirect_url)
    else:
        appointments = Appointment.objects.filter(status=True).order_by('appointment_date')
        person = Person.objects.get(username=request.session.get('username'))
        return render(request, 'doctor-home.html',context={"person":person, "appointments": appointments})
    
    
