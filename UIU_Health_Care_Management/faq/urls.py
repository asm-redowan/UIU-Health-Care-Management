from django.urls import path
from  .views import *

urlpatterns = [
    path('', qu_ans, name='faq'),
    # path('patientprofile/<username>/', patientprofile, name='patientprofile'),
    # path('info/', info, name='info'),
    # path('logout/', logout, name='logout'),
]
