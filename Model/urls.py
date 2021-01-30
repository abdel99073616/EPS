from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('' , frist_page , name='frist_page'),
    path('user_home/', User_Home, name='user_home'),
    path('admin_home/', Admin_Home, name='admin_Home'),
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout1, name='logout'),
    path('form/',Form,name='Form'),
    path('MathForm/',MathForm,name='MathForm'),
    path('AcademicForm/', AcademicForm, name='AcademicForm'),
    path('ProgramingForm/', ProgramingForm, name='ProgramingForm'),
    path('reset_password/', auth_views.PasswordResetView.as_view() , name = 'password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view() ,name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() , name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() , name = 'password_reset_complete'),
]


