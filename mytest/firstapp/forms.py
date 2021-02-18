from .models import FirstApp
from django import forms

class FirstAppForm(forms.ModelForm):
    """ Форма записей """

    class Meta:
        model = FirstApp
        fields = '__all__'
        #fields = ['title', 'description']