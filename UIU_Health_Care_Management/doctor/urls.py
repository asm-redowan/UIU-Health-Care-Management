from django.urls import path
from  .views import *

urlpatterns = [
    path('', doctor_home, name='doctor-home'),
    path('patientprofile/<username>/', patientprofile, name='patientprofile'),
    path('addprescription/<username>/', addprescription, name='addprescription'),
    path('viewprescription/<prescription_id>/', viewprescription, name='viewprescription'),
    path('save',save,name='save'),
    path('nearesthospital',nearesthospital,name='nearesthospital'),
    path('search',search,name='search'),
    # path('info/', info, name='info'),
    # path('logout/', logout, name='logout'),
]
