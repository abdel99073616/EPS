from django.shortcuts import render
from django.contrib import auth
from numpy.core.fromnumeric import cumprod
from .models import Student
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .form import CreateUserForm , StudentObj
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import *

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import svm
from sklearn.svm import SVC

# Create your views here.

Data = pd.read_csv(r'https://raw.githubusercontent.com/abdel99073616/Data/main/datalast.csv')
X1 = Data.drop(["Departments"], axis=1)
X = X1
y = Data["Departments"]

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.info(request , 'Username Or Password is invalid')
    context = {}
    return render(request , 'login.html' , context)


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           return redirect('login')
    context = {'form':form}
    return render(request , 'register.html', context)

@login_required(login_url='login')
def Home(request):
    return render(request,'index.html')

def logout1(request):
    logout(request)
    return  redirect('login')


@login_required(login_url='login')
def Form(request,pk):
    student = Student.objects.get(user = pk)
    formset = StudentObj(instance= student)
    if request.method == 'POST':
        formset = StudentObj(request.POST, instance=student)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    context = {'forms': formset}
    return render(request, 'from1.html', context)

def WECode(request,pk):
    student = Student.objects.get(user=pk)
    CS_Mat = np.array([
        student.Calculus > 99,
        student.DataBase < 90,
        student.LinerAlgebra > 99,
        student.Intro_to_CS  > 99,
        student.Intro_to_IS  < 90,
        student.Discrete_Math > 99,
        student.ObjectOriented  > 99,
        student.Statistics  > 99,
        student.ProgramingLanguage  > 99,
        student.DifferentialEquation   > 99,
        student.DataStructure   > 102,
        student.FileProcessing   < 99,
        student.AdvancedMathematics   < 99,
        student.Physics   > 99,
        student.Stochastic  < 99,
        student.Multimedia   > 99,
        student.InformationTheory  < 99,
        student.SystemAnalysis_And_Design   < 99,
        ])
    IS_Mat = np.array([
     student.Calculus < 99 ,
     student.DataBase      >90 ,
     student.LinerAlgebra  <90 ,
     student.Intro_to_CS    < 99 ,
     student.Intro_to_IS    > 90 ,
     student.Discrete_Math     < 99 ,
     student.ObjectOriented   <99 ,
     student.Statistics      < 99,
     student.ProgramingLanguage  <99 ,
     student.DifferentialEquation  <99 ,
     student.DataStructure    > 102,
     student.FileProcessing   < 99,
     student.AdvancedMathematics > 99,
     student.Physics    < 99,
     student.Stochastic  < 99,
     student.Multimedia  > 99,
     student.InformationTheory < 99,
     student.SystemAnalysis_And_Design > 99
    ])
    Department = ""
    s2 = sum(CS_Mat.astype(int))
    s3 = sum(IS_Mat.astype(int))
    if (s2 == max(s2, s3)):
        Department = "CS"
    else:
        Department = "IS"
    formset = StudentObj(instance=student)
    formset = StudentObj(request.POST, instance=student)
    formset.save()
    redirect('home')
    context = {}
    return render(request , 'Dep.html',context)
@login_required(login_url='login')
def DecisionTree(request):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    Dep_pred = clf.predict()
    return render(request , 'from1.html' )


@login_required(login_url='login')
def SVM(request):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)
    svm = SVC(kernel="linear", C=0.025, random_state=101)
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    return render(request , 'from1.html' )
