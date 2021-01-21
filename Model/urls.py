from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('login/',loginpage,name ='login'),
    path('ragister/' , register , name = 'register'),
    path('' , Home , name = 'home'),
]
