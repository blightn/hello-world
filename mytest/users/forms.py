from django import forms # Проверить необходимость.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
class UserRegistrationForm(forms.ModelForm):
    # Форма регистрации пользователя

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        #fields = '__all__'
        fields = ('username', 'first_name', 'email') # Везде поменять на кортежи.

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
"""

class UserRegistrationForm(UserCreationForm):
    # Форма регистрации пользователя

    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', ) # Везде поменять на кортежи.