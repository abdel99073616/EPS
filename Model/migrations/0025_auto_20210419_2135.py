# Generated by Django 3.2 on 2021-04-19 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0024_auto_20210419_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Bady', models.TextField(max_length=5000, null=True)),
                ('Correct_Answer_letter', models.CharField(max_length=20, null=True)),
                ('User_Answer_letter', models.CharField(max_length=20, null=True)),
                ('Status', models.CharField(choices=[('Programing', 'Programing'), ('Data Structure', 'Data Structure'), ('Linear Math', 'Linear Math'), ('Advanced Math', 'Advanced Math')], max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='QQQQQ',
        ),
    ]