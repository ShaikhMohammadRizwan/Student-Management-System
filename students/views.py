from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from django.urls import reverse  # Corrected import for reverse
from .forms import StudentForm

# Create your views here.

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)  # Fixed variable name (lowercase 'student')
    return HttpResponseRedirect(reverse('index'))  # Corrected use of reverse

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Extracting data from the form
            new_student = Student(
                student_number=form.cleaned_data['student_number'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                field_of_study=form.cleaned_data['field_of_study'],
                gpa=form.cleaned_data['gpa'],
            )
            new_student.save()  # Save the new student to the database
            return render(request, 'students/add.html', {
                'form': StudentForm(),  # Return a fresh form
                'success': 'Student added successfully!'
            })
    else:
        form = StudentForm()

    # Always render the form for GET request or in case of form errors
    return render(request, 'students/add.html', {'form': form})
