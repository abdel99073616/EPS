from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.
from .form import CreateUserForm , StudentObj
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import svm
from sklearn.svm import SVC
# Create your views here.

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
def table(request):
    return render(request,'table.html')

def Form(request):
    form = StudentObj()
    if request.method == "POST":
        form = StudentObj(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    context = {'forms': form}
    return render(request, 'from1.html', context)


def WECode(request):
    Department = "IS"
    if request.method == "POST":
        Calculus     = int(request.POST.get('Calculus'))
        DataBase    = int(request.POST.get('DataBase'))
        Liner       = int(request.POST.get('Liner Algebra'))
        intro_cs    = int(request.POST.get('intro to computer sceince'))
        intro_is    = int(request.POST.get('intro to IS'))
        dis         = int(request.POST.get('Discrete'))
        oop         = int(request.POST.get('Object Oriented'))
        statis     = int(request.POST.get('Statistics'))
        programing    = int(request.POST.get('Computer Programing'))
        DE          = int(request.POST.get('Defferental Equation'))
        OR          = int(request.POST.get('Operations Researsh'))
        DS          = int(request.POST.get('Data Strucure'))
        FP          = int(request.POST.get('File Processing'))
        AM          = int(request.POST.get('Advansed Mathematics'))
        PY          = int(request.POST.get('Physic'))
        ST          = int(request.POST.get('Stotastic'))
        MATH    = int(request.POST.get('Multimedia'))
        IT      = int(request.POST.get('information theory'))
        SA      = int(request.POST.get('system analysis and design'))
        management = int(request.POST.get('Management'))
        problem_solving = int(request.POST.get('ProblemSolving'))


        CS_Mat = np.array([
            Calculus > 99,
            DataBase < 90,
            Liner > 99,
            intro_cs  > 99,
            intro_is  < 90,
            dis > 99,
            oop  > 99,
            statis  > 99,
            programing  > 99,
            DE   > 99,
            OR   > 102,
            DS   < 99,
            FP   < 99,
            AM   > 99,
            PY  < 99,
            ST   > 99,
            MATH  < 99,
            IT   < 99,
            SA  < 99,
            management > 99,
            problem_solving >99
        ])
        IS_Mat = np.array([
            Calculus  < 99 ,
            DataBase  >90 ,
            Liner <90 ,
            intro_cs < 99 ,
            intro_is > 90 ,
            dis < 99 ,
            oop  <99 ,
            statis < 99,
            programing <99 ,
            DE  <99 ,
            OR  > 102 ,
            DS < 99 ,
            FP > 99 ,
            AM < 99,
            PY < 99 ,
            ST > 99,
            MATH <99,
            IT >99 ,
            SA >99 ,
            management > 99,
            problem_solving > 99
        ])

        s2 = sum(CS_Mat.astype(int))
        s3 = sum(IS_Mat.astype(int))
        if (s2 == max(s2, s3)):
            Department = "CS"
    context = {'Department':Department}

    return render(request , 'from1.html' , context)

def DecisionTree(request):
    pima = pd.read_csv(r'https://raw.githubusercontent.com/abdel99073616/Data/main/datalast.csv')
    X1 = pima.drop(["Departments"], axis=1)
    X = X1
    y = pima["Departments"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/249,random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    E_text = pd.read_csv(r'https://raw.githubusercontent.com/abdel99073616/Data/main/datalast2.csv')
    y_pred = clf.predict(E_text)

    context= {'data':y_pred}
    return render(request , 'index.html' , context)


def SVM(request):
    pima = pd.read_csv(r'https://raw.githubusercontent.com/abdel99073616/Data/main/datalast.csv')
    X1 = pima.drop(["Departments"], axis=1)
    X = X1
    y = pima["Departments"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)

    svm = SVC(kernel="linear", C=0.025, random_state=101)
    svm.fit(X_train, y_train)
    E_text = pd.read_csv(r'https://raw.githubusercontent.com/abdel99073616/Data/main/datalast2.csv')
    y_pred = svm.predict(E_text)
    context= {'data':y_pred}
    return render(request , 'index.html' , context)
