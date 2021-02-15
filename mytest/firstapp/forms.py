from .models import FirstApp
from django import forms

class FirstAppForm(forms.ModelForm):
    """ Форма """

    class Meta:
        model = FirstApp
        fields = '__all__'
        #fields = ['title', 'description']
        #fields = ('Заголовок', 'Описание')