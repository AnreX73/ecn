from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from ecn.forms import UserCreationForm


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
            return redirect('home')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
