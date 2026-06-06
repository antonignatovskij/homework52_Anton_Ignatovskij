from django import forms
from django.forms.widgets import Textarea, TextInput

CHOICES = [('new','новая'),('in_progress','в процессе'),('done','сделано')]
class TaskForm(forms.Form):
    description = forms.CharField(widget=TextInput(attrs={"class":"form-control"}), required=True, label="Описание", error_messages={"required":"Описание - обязательное поле"})
    detail_description = forms.CharField(widget=Textarea(attrs={"class":"form-control"}), required=False, label="Подробнее")
    date = forms.CharField(widget=TextInput(attrs={"class":"form-control"}), required=True, label="Выполнить до", error_messages={"required":"Дедлайн - обязательное поле"})
    status = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-select"}),choices=CHOICES)