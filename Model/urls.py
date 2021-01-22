from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', Home, name='home'),
    path('login/', loginpage, name='login'),
    path('table/', table, name='table'),
    path('ragister/', register, name='register'),
    path('logout/', logout1, name='logout'),
]
