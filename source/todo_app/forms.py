from django import forms
from django.forms import widgets
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from todo_app.models import TodoItem
from django.forms.widgets import Textarea, TextInput

class TaskForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ['description','detail_description','date','status']

        widgets = {
            # "description": widgets.Input(attrs={'class':'form-control'}),
            # "detail_description": widgets.Textarea(attrs={'cols':40,'rows':5}),
            # "date": widgets.Input(attrs={'class': 'form-control'}),
            # "status": widgets.Select(attrs={'class': 'form-control'}),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description == 'test400':
            raise forms.ValidationError('test400')
        return description



