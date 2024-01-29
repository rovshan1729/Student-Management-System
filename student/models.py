from django.db import models

class Student(models.Model):
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'