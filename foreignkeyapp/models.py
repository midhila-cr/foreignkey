from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255,null=True)
    fee = models.IntegerField(null=True)
    def __str__(self):
        return self.course_name
class Student(models.Model):
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        null=True
    )
    student_name = models.CharField(
        max_length=255,null=True
    )
    student_address = models.CharField(
        max_length=255,null=True
    )
    student_age = models.IntegerField(
        null=True, 
        blank=True
    )
    joining_date = models.DateField(null=True)
    def __str__(self):
        return self.student_name


# Create your models here.
