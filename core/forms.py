from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CourseForm(forms.ModelForm):
    add_more = forms.CharField(widget=forms.Textarea, help_text="add comma separated lessons here")

    class Meta:
        model = Course
        fields = ['title','description','image','lessons']
        labels={
            "title": "Course Title"
        }
