from django.urls import path
from  .views import *

urlpatterns = [
    path('', patient_home, name='patient-home'),
    # path('info/', info, name='info'),
    # path('logout/', logout, name='logout'),
    
]
