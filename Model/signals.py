from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import User


def create_Student(sender,instance , created , **kwargs):
    if created:
        Student.objects.create(
            user=instance,
        )
post_save.connect(create_Student , sender= User)

