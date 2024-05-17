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

def menu(request):
    context={
        'products': [
        {'name': 'Classic Burger', 'price': 50.0},
        {'name': 'Cheeseburger', 'price': 55.0},
        {'name': 'Double Burger', 'price': 70.0},
        {'name': 'French Fries', 'price': 30.0},
        {'name': 'Onion Rings', 'price': 35.0},
        {'name': 'Chicken Nuggets', 'price': 40.0},
        {'name': 'Hot Dog', 'price': 25.0},
        {'name': 'Chicken Sandwich', 'price': 60.0},
        {'name': 'Caesar Salad', 'price': 45.0},
        {'name': 'Vanilla Milkshake', 'price': 40.0},
        {'name': 'Chocolate Milkshake', 'price': 40.0},
        {'name': 'Strawberry Milkshake', 'price': 40.0},
        {'name': 'Cola Drink', 'price': 20.0},
        {'name': 'Orange Soda', 'price': 20.0},
        {'name': 'Mineral Water', 'price': 15.0},
    ]
    }
    return render(request, 'web/menu.html', context)