from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from user_account.forms import UserAccountRegistrationForm, UserAccountProfileForm


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserAccountRegistrationForm

    def get_success_url(self):
        return reverse('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = "Register new user"
        return context


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title': 'Login as user'}

    def get_success_url(self):
        return reverse('index')


class UserAccountLogoutView(LogoutView):
    template_name = 'logout.html'
    extra_context = {'title': 'Logout'}

    def get_success_url(self):
        return reverse('index')


class UserAccountProfileView(UpdateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Profile'}
    form_class = UserAccountProfileForm

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user
