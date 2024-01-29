from django import forms
from .models import Student

class StudentForm(forms.Form):
    model = Student
    fields = "__all__"
