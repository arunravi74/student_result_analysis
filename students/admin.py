from django.contrib import admin

from students.models import student_list, student_mark

# Register your models here.
admin.site.register(student_list)
admin.site.register(student_mark)