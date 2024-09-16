from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Students

# View to display a list of all students
def student_list(request):
    students = Students.objects.all()
    return render(request, 'records/student_list.html', {'students': students})

# View to display details of a single student
def student_detail(request, student_id):
    student = get_object_or_404(Students, student_id=student_id)
    return render(request, 'records/student_detail.html', {'student': student})

# View to create a new student
def create_students(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if not student_id:
            return render(request, 'students/form.html', {
                'form_title': 'Add Student',
                'error': 'Student ID cannot be empty.'
            })

        if Students.objects.filter(student_id=student_id).exists():
            return render(request, 'students/form.html', {
                'form_title': 'Add Student',
                'error': 'Student ID already exists. Please choose a different ID.'
            })

        student = Students(
            student_id=student_id,
            name=request.POST.get('name'),
            father_name=request.POST.get('father_name'),  # New field
            which_class=request.POST.get('which_class'),
            age=request.POST.get('age'),
            contact=request.POST.get('contact')
        )
        student.save()
        return redirect(reverse('student_list'))
    
    return render(request, 'records/student_form.html', {'form_title': 'Add Student'})

def edit_student(request, student_id):
    student = get_object_or_404(Students, student_id=student_id)

    if request.method == 'POST':
        new_student_id = request.POST.get('student_id')
        if not new_student_id:
            return render(request, 'students/form.html', {
                'form_title': 'Edit Student',
                'student': student,
                'error': 'Student ID cannot be empty.'
            })

        if new_student_id != student_id and Students.objects.filter(student_id=new_student_id).exists():
            return render(request, 'students/form.html', {
                'form_title': 'Edit Student',
                'student': student,
                'error': 'Student ID already exists. Please choose a different ID.'
            })

        student.student_id = new_student_id
        student.name = request.POST.get('name')
        student.father_name = request.POST.get('father_name')  # New field
        student.which_class = request.POST.get('which_class')
        student.age = request.POST.get('age')
        student.contact = request.POST.get('contact')
        student.save()

        return redirect(reverse('student_list'))
    
    return render(request, 'records/student_form.html', {'form_title': 'Edit Student', 'student': student})

# View to delete a student
def delete_student(request, student_id):
    student = get_object_or_404(Students, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect(reverse('student_list'))
    return render(request, 'records/student_confirm_delete.html', {'student': student})