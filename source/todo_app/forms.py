from django import forms
from django.core.validators import MinValueValidator
from django.forms import widgets

from todo_app.models import TodoItem

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = TodoItem
        fields = ('title', 'description', 'status', 'type')
        widgets = {}
