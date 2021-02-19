from .models import FirstApp
from django import forms

class FirstAppForm(forms.ModelForm):
    """ Форма записи """

    class Meta:
        model = FirstApp
        fields = '__all__'
        #fields = ['title', 'description']