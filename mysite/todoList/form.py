from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название задачи'}),
            'completed': forms.CheckboxInput(),
        }
