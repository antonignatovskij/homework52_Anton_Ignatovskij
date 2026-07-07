from django import forms
from django.forms import widgets

from todo_app.models import TodoItem, Status


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TodoItem
        fields = ('title', 'description', 'status', 'type')
        widgets = {
            'title' : widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class':'form-control','cols': '40', 'rows': '5'}),
            'status': widgets.Select(attrs={'class': 'form-select'}),
            'type': widgets.CheckboxSelectMultiple()
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Заголовок задачи должен быть не менее трех символов")
        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if description:
            if len(description) < 10:
                raise forms.ValidationError("Заголовок описания должен быть не менее десяти символов")
        return description
