from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
#from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from .forms import UserRegistrationForm
from mytest.tokens import account_activation_token


def register_OLD(request):
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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect(reverse_lazy('users:account_activation_sent'))
    else:
        form = UserRegistrationForm()
        
    return render(request, 'users/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        return redirect(reverse_lazy('users:register_done'))
    else:
        return render(request, 'users/account_activation_invalid.html')