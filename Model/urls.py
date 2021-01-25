from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home, name='home'),
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout1, name='logout'),
    path('form/',Form,name='Form'),
    path('reset_password/', auth_views.PasswordResetView.as_view() , name = 'password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view() ,name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() , name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() , name = 'password_reset_complete'),
]


