from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student
from django import forms
from django.forms.widgets import TextInput  , EmailInput , PasswordInput
from django.forms import inlineformset_factory



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' ,'first_name','last_name', 'password1' , 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control',}),
            'email': EmailInput(attrs={'class': 'form-control',}),
            'first_name': TextInput(attrs={'class': 'form-control',}),
            'last_name': TextInput(attrs={'class': 'form-control',}),
            'password1': PasswordInput(attrs={'class': 'form-control',}),
            'password2': PasswordInput(attrs={'class': 'form-control',}),
        }

class StudentObj(forms.ModelForm):
    class Meta:
        model = Student
        fields =['Calculus','DataBase','LinerAlgebra','Intro_to_CS','Intro_to_IS',
                  'Discrete_Math','ObjectOriented','Statistics','ProgramingLanguage',
                  'DifferentialEquation','Operations_Researsh','DataStructure','FileProcessing','AdvancedMathematics',
                  'Physics','Stochastic','Multimedia','InformationTheory','SystemAnalysis_And_Design'
                  ]
