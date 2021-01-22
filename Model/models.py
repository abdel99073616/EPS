from django.db import models
from django.contrib.auth.models import User


# This Model will be split to two categories:
# - Historical Education Models.
# - EPS Quizes.

class Student(models.Model):
    user = models.OneToOneField(User, null=True ,blank = True , on_delete=models.CASCADE)
    #name = models.CharField(max_length=100 , null=True)
    #email = models.CharField(max_length=200 , null= True)

    # - Historical Education Models.

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
    DataStructure = models.PositiveIntegerField(null=True)
    FileProcessing = models.PositiveIntegerField(null=True)
    AdvancedMathematics = models.PositiveIntegerField(null=True)
    Physics = models.PositiveIntegerField(null=True)
    Stochastic = models.PositiveIntegerField(null=True)
    Multimedia = models.PositiveIntegerField(null=True)
    InformationTheory = models.PositiveIntegerField(null=True)
    SystemAnalysis_And_Design = models.PositiveIntegerField(null=True)
    Department = models.CharField(max_length=10,null =True)

    # - EPS Quizes.


    def __str__(self):
        return self.name
