from django.shortcuts import render
from django.contrib import auth
from numpy.core.fromnumeric import cumprod
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .form import *
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import *
from .decorators import unauthenticated_user , allowed_users , admin_only
from django.views.generic import ListView
from django.http import JsonResponse


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




def frist_page(request):
    return render(request , 'FristPage.html')

@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect("admin_Home")
        else:
            messages.info(request , 'Username Or Password is invalid')
    context = {}
    return render(request , 'login.html' , context)

@unauthenticated_user
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
@allowed_users(allowed_roles=['student'])
def User_Home(request):
    pk = request.user.id
    student = Student.objects.get(user = pk)
    context = {'student' : student}
    return render(request, 'user_home.html', context)

@login_required(login_url='login')
@admin_only
def Admin_Home(request):
    return render(request, 'admin_home.html')

def logout1(request):
    logout(request)
    return  redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def Form(request):
    pk = request.user.id
    student = Student.objects.get(user = pk)
    formset = StudentObj(instance= student)
    if request.method == 'POST':
        formset = StudentObj(request.POST, instance=student)
        if formset.is_valid():
            formset.save()
            WECode(request)
            DecisionTree(request)
            SVM(request)
            return redirect('user_home')

    context = {'forms': formset}
    return render(request, 'from1.html', context)


def WECode(request):
    pk = request.user.id
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
        student.Operations_Researsh >102 ,
        student.DataStructure   < 99 ,
        student.FileProcessing   < 99,
        student.AdvancedMathematics   > 99,
        student.Physics   > 99,
        student.Stochastic  > 99,
        student.Multimedia   < 99,
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
     student.Operations_Researsh <102 ,
     student.DataStructure    < 99,
     student.FileProcessing   > 99,
     student.AdvancedMathematics < 99,
     student.Physics    < 99,
     student.Stochastic  < 99,
     student.Multimedia  > 99,
     student.InformationTheory > 99,
     student.SystemAnalysis_And_Design > 99
    ])
    s2 = sum(CS_Mat.astype(int))
    s3 = sum(IS_Mat.astype(int))
    if (s2 == max(s2, s3)):
        student.Department_WE = "CS"
    else:
        student.Department_WE = "IS"
    form = StudentObj(instance=student)
    form = StudentObj(request.POST, instance=student)
    if form.is_valid():
        form.save()
    return request

Data = pd.read_csv(r'https://raw.githubusercontent.com/abdel99073616/Data/main/datalast.csv')
X = Data.drop(["Departments"], axis=1)
y = Data["Departments"]


@login_required(login_url='login')
def DecisionTree(request):
    pk = request.user.id
    student = Student.objects.get(user=pk)
    df = pd.DataFrame(list(Student.objects.all().values()))
    df = df.loc[df['user_id'] == pk]
    df = df.drop(["user_id" , "id" , "Department_WE", "Department_DS","Department_SVM"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    Dep_pred = clf.predict(df)
    student.Department_DS = list(Dep_pred)[0]
    form = StudentObj(instance=student)
    form = StudentObj(request.POST, instance=student)
    if form.is_valid():
        form.save()
    return request


@login_required(login_url='login')
def SVM(request):
    pk = request.user.id
    student = Student.objects.get(user=pk)
    df = pd.DataFrame(list(Student.objects.all().values()))
    df = df.loc[df['user_id'] == pk]
    df = df.drop(["user_id", "id", "Department_WE", "Department_DS", "Department_SVM"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)
    svm = SVC(kernel="linear", C=0.025, random_state=101)
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    Dep_pred = svm.predict(df)
    student.Department_SVM = list(Dep_pred)[0]
    form = StudentObj(instance=student)
    form = StudentObj(request.POST, instance=student)
    if form.is_valid():
        form.save()
    return request

@login_required(login_url='login')
def Quiz1 (request):
    quiz1 = Quiz.objects.filter(kind = 'Programing')
    quiz2 = Quiz.objects.filter(kind='Linear Math')
    context = {'quiz1':quiz1 , 'quiz2':quiz2}
    return render(request, 'Quiz1.html', context)


class QuizListVeiw(ListView):
    model = Quiz_2
    template_name = 'quizes/quiz.html'

def quiz_veiw(request):
    quiz = Quiz_2.objects.all()
    context = {'obj':quiz}
    return render (request, 'quizes/main.html', context)

def quizpk_veiw(request , pk):
    quiz = Quiz_2.objects.get(pk = pk)
    context = {'obj':quiz}
    return render (request, 'quizes/quiz.html', context)

def quiz_data_view(request , pk):
    quiz = Quiz_2.objects.get(pk =pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answer():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse({
        'data' : questions,
        'time' : quiz.time
    })













