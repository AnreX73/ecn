from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from ecn.forms import UserCreationForm, UserLoginForm, UserPasswordResetForm


def index(request):
    context = {
        'title': 'Агенство ЕЦН',

    }
    return render(request, 'ecn/index.html', context=context)


def about(request):
    context = {
        'title': 'О нас',

    }
    return render(request, 'ecn/about.html', context=context)


def profile(request):
    context = {
        'title': 'Your page',

    }
    return render(request, 'registration/profile.html', context=context)


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
            'title': 'регистрация',
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class UserLogin(LoginView):
    template_name = 'registration/user_login.html'
    form_class = UserLoginForm


class UserPasswordReset(PasswordResetView):
    template_name = 'registration/user_password_reset.html'
    form_class = UserPasswordResetForm

    def get_success_url(self):
        return reverse_lazy('user_password_reset_done')


class UserPasswordResetDone(PasswordResetDoneView):
    template_name = 'registration/user_password_reset_done.html'

