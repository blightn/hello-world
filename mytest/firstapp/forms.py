from .models import Note
from django import forms

class FirstAppForm(forms.ModelForm):
    # Форма создания/изменения записки

    class Meta:
        model = Note
        fields = '__all__'
        #fields = ['title', 'text']