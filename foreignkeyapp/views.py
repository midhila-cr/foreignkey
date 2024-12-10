from django.shortcuts import render,redirect,get_object_or_404
from .import views
from foreignkeyapp.models import Course
from foreignkeyapp.models import Student
def home(request):
    return render(request,"home.html")
def addcourses(request):
    return render(request,"addcourse.html")


def addcourse(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')  # Retrieves the course name from the form
        course_fee = request.POST.get('course_fee')  # Retrieves the fee from the form

        # Create a new Course object and save it to the database
        course = Course(course_name=course_name, fee=course_fee)
        course.save()

        # Redirect to the home page or another URL after saving
        return redirect('addcourses')

def addstudent(request):
    courses=Course.objects.all()
    return render(request,'addstudent.html',{'course': courses})
def addstudentdb(request):
        if request.method == 'POST':
            student_name = request.POST['student_name']
            student_address = request.POST['address']
            age = request.POST['age']
            jdate = request.POST['dob']
            sel = request.POST['course']

            print(sel)
            course = Course.objects.get(id=sel)
            print(course)
            
            student = Student(
                student_name=student_name,
                student_address=student_address,
                student_age=age,
                course=course,
                joining_date=jdate
            )
            student.save()
            return redirect('show_details')


def show_details(request):
    students=Student.objects.all()
    return render(request,'showstudent.html', {'students': students})
def delete(request,pk):
    s = Student.objects.get(id=pk)
    s.delete()
    return redirect('show_details')
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()
    
    if request.method == "POST":
        # Get data from the form
        student.student_name = request.POST.get('student_name')
        student.student_address = request.POST.get('address')
        student.student_age = request.POST.get('age')
        student.joining_date = request.POST.get('dob')
        course_id = request.POST.get('course')
        student.course = get_object_or_404(Course, id=course_id)
        student.save()  # Save changes to the database
        return redirect('show_details')  
    
    return render(request, 'edit.html', {
        'student': student,
        'courses': courses,
    })

