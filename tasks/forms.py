from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Task, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False
    )

    class Meta:
        model = Task
        fields = ["title", "description", "status", "due_date"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]