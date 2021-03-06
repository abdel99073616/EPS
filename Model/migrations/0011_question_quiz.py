# Generated by Django 3.2 on 2021-04-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0010_alter_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(to='Model.Question')),
            ],
        ),
    ]
