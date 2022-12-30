from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm


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
