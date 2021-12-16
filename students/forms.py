from django import forms
from students.models import student_list
from result_analysis import settings

class studentlist_form(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats= settings.DATE_INPUT_FORMATS,initial='YYYY-MM-DD')
    class Meta:
        model = student_list
        fields = '__all__'
