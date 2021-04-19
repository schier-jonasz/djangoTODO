from django import forms
from django.forms import widgets
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            "taskTitle": forms.TextInput(attrs = {'class': 'form__title',
                            'placeholder': 'Enter task...'}),
            "complete": forms.CheckboxInput(attrs = {'class': 'form__checkbox'}),
        }



