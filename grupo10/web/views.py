from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect


def index(request):
    context={
        'nombre': 'Ernesto',
    }

    return render(request, 'web/index.html', context)

def clientForm(request):
    context={}

    if (request.method == "GET"):
        context['clientForm'] = ClientForm()
    
    else:
        context['clientForm'] = ClientForm(request.POST)

        print(request.POST)

        return redirect('index')

    return render(request, 'web/clientForm.html', context)
