from django import forms
from main_project_fldr.core.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('description', 'is_completed')