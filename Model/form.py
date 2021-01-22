from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student
from django import forms
from django.forms.widgets import TextInput  , EmailInput , PasswordInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' ,'first_name','last_name', 'password1' , 'password2']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'User Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
            'password1': PasswordInput(),
            'password2': PasswordInput(),
        }
class StudentObj(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Calculus','DataBase','LinerAlgebra','Intro_to_CS','Intro_to_IS',
                  'Discrete_Math','ObjectOriented','Statistics','ProgramingLanguage',
                  'DifferentialEquation','DataStructure','FileProcessing','AdvancedMathematics',
                  'Physics','Stochastic','Multimedia','InformationTheory','SystemAnalysis_And_Design'
                  ]

        #labels = {'Calculus': _('New renewal date')}
        #help_texts = {'Calculus': _('Enter a date between now and 4 weeks (default 3).')}
