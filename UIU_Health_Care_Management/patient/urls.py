from django.urls import path
from  .views import *

urlpatterns = [
    path('', patient_home, name='patient-home'),
    path('appointment/', take_appointment, name='take-appoinment'),
    path('prescriptionlist/',prescriptionlist, name='prescriptionlist'),
    # path('info/', info, name='info'),
    # path('logout/', logout, name='logout'),
    
]
