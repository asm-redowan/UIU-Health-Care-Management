from django.shortcuts import render

# Create your views here.
def doctor_home(request):
    return render(request, 'doctor-home.html')
