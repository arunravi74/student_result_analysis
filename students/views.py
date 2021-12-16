from django.views import  View
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from students.forms import studentlist_form

from students.models import student_list,student_mark


class studentlist_view(View):
    form_class = studentlist_form
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        students = student_list.objects.all().order_by('id')
        form = self.form_class()
        return render(request, self.template_name, {'students': students,'form':form})

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/student')
        return render(request, self.template_name, {'form': form})


def studentmark_view(request,pk): 
    data = get_object_or_404(student_list,id=pk)
    student_id = data.id
    if request.method=="POST":
        student = student_mark.objects.filter(student_id=data.id)
        if not student:
            marks = request.POST.get('marks')

            out = student_mark(marks=marks,student_id=student_id)
            out.save()
            return redirect('student_list')
            HttpResponse(f'successfully added marks to user {data.name}')
        else:
            return HttpResponse(f'Mark already added to this user {data.name}')
    return render(request, 'add_marks.html')


def studentmark_detailview(request,pk):
    data = student_mark.objects.raw(f"""SELECT 
    students_student_list.id,students_student_list.name,students_student_mark.marks 
    FROM students_student_list INNER JOIN students_student_mark ON 
    students_student_mark.student_id = students_student_list.id where students_student_list.id={pk}""")    
    return render(request,'student_detail.html',{'data':data})

def studentresult_view(request):
    data = student_list.objects.all().count()
    mark = student_mark.objects.all()
    print(mark)
    
    l = {}.fromkeys(['A', 'B', 'C', 'D', 'E', 'F'], 0)
    count = len(mark[:])
    print(count)
    for i in range(0,count):
        if 91<=mark[i].marks<=100:
            grade = 'A'
            l['A'] += 1           
        elif 81<=mark[i].marks<=90:
            grade = 'B'
            l['B'] += 1
        elif 71<=mark[i].marks<=80:
            grade = 'C'
            l['C'] += 1
        elif 61<=mark[i].marks<=70:
            grade = 'D'
            l['D'] += 1
        elif 51<=mark[i].marks<=60:
            grade = 'E'
            l['E'] += 1
        else:
            grade = 'F'
            l['F'] += 1
    distinction = (l['A'] / count) * 100
    first_class = ((l['B']+l['C'])/count) * 100
    _pass = ((count - l['F'])/count) * 100            
    return render(request,'student_result.html',
    {'data':data,'mark':mark,'grade':l,'distinction':distinction,'first_class':first_class,'pass':_pass})

    
