from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #new_user = form.save()
            form.save()

            """
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse_lazy('firstapp:list'))
            """

            #return render(request, 'users/register_done.html', {'new_user': new_user})
            return redirect(reverse_lazy('users:register_done'))
    else:
        form = UserRegistrationForm()
        
    return render(request, 'users/register.html', {'form': form})