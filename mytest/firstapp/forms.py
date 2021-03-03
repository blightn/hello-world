from django import forms

from .models import Note

class FirstAppForm(forms.ModelForm):
    # Форма создания/изменения записки

    class Meta:
        model = Note
        fields = '__all__'
        #fields = ['title', 'text']