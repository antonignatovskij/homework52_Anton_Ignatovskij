from django import forms
from django.forms import widgets

from todo_app.models import TodoItem, Type, Status

class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = TodoItem
        fields = ('title', 'description', 'status', 'type')
        widgets = {
            'description': widgets.Textarea(attrs={'cols': '40', 'rows': '5'}),
        }
