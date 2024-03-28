from django.urls import path
from  .views import *

urlpatterns = [
    path('', login_page, name='login_page'),
    path('info/', info, name='info'),
    path('logout/', logout, name='logout'),
    
]
