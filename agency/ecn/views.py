from django.shortcuts import render


def index(request):
    context = {
        'title': 'Агенство ЕЦН',

    }
    return render(request, 'ecn/index.html', context=context)
