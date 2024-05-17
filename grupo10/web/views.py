from django.shortcuts import render

def index(request):
    context={
        'nombre': 'Ernesto',
    }

    return render(request, 'web/index.html', context)
