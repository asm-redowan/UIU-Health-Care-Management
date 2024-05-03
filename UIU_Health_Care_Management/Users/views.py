from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout
from django.contrib.sessions.models import Session
from .models import Person
from django.contrib.auth.decorators import login_required
# Create your views here.

def custom_authentication(username, password):
    try:
        user = Person.objects.get(username=username)
        if user.password==password:  # Use Django's check_password function for secure password comparison
            return user  # User authenticated successfully
        else:
            return None  # Incorrect password

    except Person.DoesNotExist:
        return None  # User does not exist

def login_page(request):
    if request.method == "POST":
        username =  request.POST['username']
        password =  request.POST['password']

        user = custom_authentication(username, password)

        if user is not None:
            request.session['username']=user.username
            request.session['usertype']=user.usertype
            # print(user.usertype)
            if user.usertype=="Doctor":
                return redirect('doctor-home')
            else:
                return redirect('patient-home')
        else:
            print("no")

    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    # Redirect to a success page or homepage
    return redirect('index')


def index(request):
    return render(request, 'index.html')


# def info(request):
#     if request.session.get('username') is None:
#         return redirect('login_page')
#     return render(request, 'info.html')
