from django.db import models
from django.contrib.auth.models import User


# This Model will be split to two categories:
# - Historical Education Models.
# - EPS Quizes.


class Student (models.Model):
    user = models.OneToOneField(User  , on_delete=models.CASCADE)
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

class Math(models.Model):
    userMath = models.OneToOneField(User  , on_delete=models.CASCADE)
    LinerAlgebra = models.PositiveIntegerField(null=True)
    Discrete_Math = models.PositiveIntegerField(null=True)
    DifferentialEquation = models.PositiveIntegerField(null=True)
    AdvancedMathematics = models.PositiveIntegerField(null=True)
    Stochastic = models.PositiveIntegerField(null=True)
    Statistics = models.PositiveIntegerField(null=True)
    Calculus = models.PositiveIntegerField(null=True)
    Operations_Researsh = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.userMath.first_name + ' ' + self.userMath.last_name

class Academic(models.Model):
    userAcademic = models.OneToOneField(User  , on_delete=models.CASCADE)
    InformationTheory = models.PositiveIntegerField(null=True)
    Multimedia = models.PositiveIntegerField(null=True)
    Intro_to_IS = models.PositiveIntegerField(null=True)
    Intro_to_CS = models.PositiveIntegerField(null=True)
    SystemAnalysis_And_Design = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.userAcademic.first_name + ' ' + self.userAcademic.last_name


class Programing(models.Model):
    userPrograming = models.OneToOneField(User  , on_delete=models.CASCADE)
    ProgramingLanguage = models.PositiveIntegerField(null=True)
    DataBase = models.PositiveIntegerField(null=True)
    DataStructure = models.PositiveIntegerField(null=True)
    FileProcessing = models.PositiveIntegerField(null=True)
    ObjectOriented = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.userPrograming.first_name + ' ' + self.userPrograming.last_name


# - EPS Quizes.


#class Quizes(models.Model):

