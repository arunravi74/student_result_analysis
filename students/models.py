from django.db import models

class student_list(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    roll_number = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return str(self.id)

class student_mark(models.Model):
    student = models.OneToOneField(student_list,on_delete=models.CASCADE)
    marks = models.IntegerField()
   
