from django.urls import path
from  .views import *

urlpatterns = [
    path('', doctor_home, name='doctor-home'),
    # path('info/', info, name='info'),
    # path('logout/', logout, name='logout'),
    
]
