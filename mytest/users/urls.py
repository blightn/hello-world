from django.urls import path

from django.contrib.auth import views
from django.urls import reverse_lazy

from .views import register, activate


app_name = 'users'

urlpatterns = [
  path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),

  path('password-change/', views.PasswordChangeView.as_view(success_url=reverse_lazy('users:password_change_done'), template_name='users/password_change.html'), name='password_change'),
  path('password-change/done/', views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),

  path('password-reset/', views.PasswordResetView.as_view(email_template_name='users/password_reset_email.html', success_url=reverse_lazy('users:password_reset_done'),
    template_name='users/password_reset_form.html'), name='password_reset'),
  path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password_reset_complete'), template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
  path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

  path('register/', register, name='register'),
  path('register/activation/', views.TemplateView.as_view(template_name='users/account_activation_sent.html'), name='account_activation_sent'),
  path('register/activate/<uidb64>/<token>/', activate, name='activate'),
  path('register/done/', views.TemplateView.as_view(template_name='users/register_done.html'), name='register_done'),
]