# Generated by Django 3.2.9 on 2021-12-05 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_mark_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_mark',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student_list'),
        ),
    ]
