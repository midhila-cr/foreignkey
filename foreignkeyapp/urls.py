from .import views
from django.urls import path,include
urlpatterns = [

    path('',views.home,name='home'),
    path('addcourses',views.addcourses,name='addcourses'),



    path('addcourse',views.addcourse,name='addcourse'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addstudentdb',views.addstudentdb,name='addstudentdb'),
    path('show_details',views.show_details,name='show_details'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),

   
]