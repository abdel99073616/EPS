# Generated by Django 3.2 on 2021-04-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0022_alter_qqqqq_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qqqqq',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
