from django.urls import path
from .views import studentlist_view, studentmark_view,studentmark_detailview,studentresult_view

urlpatterns = [
    
    path('student/',studentlist_view.as_view(),name='student_list'),
    path('student/<int:pk>/marks/add/',studentmark_view,name='student_mark'),
    path('student/<int:pk>/marks/',studentmark_detailview,name='student_detailmark'),
    path('student/results/',studentresult_view,name='studentresult')   
    
]