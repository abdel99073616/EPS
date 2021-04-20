from django.db import models
from django.contrib.auth.models import User


class Student (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User  , on_delete=models.CASCADE)

    Calculus = models.PositiveIntegerField(null=True)
    DataBase = models.PositiveIntegerField(null=True)
    LinerAlgebra = models.PositiveIntegerField(null=True)
    Intro_to_CS = models.PositiveIntegerField(null=True)
    Intro_to_IS = models.PositiveIntegerField(null=True)
    Discrete_Math = models.PositiveIntegerField(null=True)
    ObjectOriented = models.PositiveIntegerField(null=True)
    Statistics = models.PositiveIntegerField(null=True)
    ProgramingLanguage = models.PositiveIntegerField(null=True)
    DifferentialEquation = models.PositiveIntegerField(null=True)
    Operations_Researsh = models.PositiveIntegerField(null=True)
    DataStructure = models.PositiveIntegerField(null=True)
    FileProcessing = models.PositiveIntegerField(null=True)
    AdvancedMathematics = models.PositiveIntegerField(null=True)
    Physics = models.PositiveIntegerField(null=True)
    Stochastic = models.PositiveIntegerField(null=True)
    Multimedia = models.PositiveIntegerField(null=True)
    InformationTheory = models.PositiveIntegerField(null=True)
    SystemAnalysis_And_Design = models.PositiveIntegerField(null=True)
    Department_WE = models.CharField(max_length=2,null =True , blank=True)
    Department_DS = models.CharField(max_length=2,null =True , blank=True)
    Department_SVM = models.CharField(max_length=2,null =True , blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Quiz(models.Model):
    Kind = (
        ('Programing', 'Programing'),
        ('Data Structure', 'Data Structure'),
        ('Linear Math', 'Linear Math'),
        ('Advanced Math', 'Advanced Math'),
    )
    id = models.AutoField(primary_key=True)
    Bady = models.TextField(max_length=5000,null=True)
    Correct_Answer_letter = models.CharField(max_length=20,null=True)
    User_Answer_letter = models.CharField(max_length=20,null=True)
    kind = models.CharField(max_length=200 , null=True, choices=Kind)

    def __str__(self):
        return self.Bady










