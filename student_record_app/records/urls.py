from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<str:student_id>/', views.student_detail, name='student_detail'),
    path('add/', views.create_students, name='create_student'),
    path('student/edit/<str:student_id>/', views.edit_student, name='edit_student'),
    path('student/delete/<str:student_id>/', views.delete_student, name='delete_student'),
]