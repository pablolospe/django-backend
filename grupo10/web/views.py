from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from .models import Product, Client
from django.views.generic.list import ListView

def index(request):
    context={}
    return render(request, 'web/index.html', context)

def clientForm(request):
    clients = Client.objects.all()
    context={'clients': clients }
    if (request.method == "GET"):
        context['clientForm'] = ClientForm()
    
    else:
        form = ClientForm(request.POST)
        context['clientForm'] = form

        if form.is_valid():
            new_client = Client(
                name= form.cleaned_data['name'],
                lastname= form.cleaned_data['lastname'],
                phone= form.cleaned_data['phone'],
                email= form.cleaned_data['email'],
                dni= form.cleaned_data['dni'],
            )
            new_client.save()

            messages.success(request, 'El cliente fue dado de alta con éxito')

            return redirect('index')

    return render(request, 'web/clientForm.html', context)

def menu(request):
    products = Product.objects.all().order_by('id')
    context = {
        'products': products
    }
    return render(request, 'web/menu.html', context)

class ClientListView(ListView):
    model=Client
    context_object_name='clients'
    template_name='web/clients.html'
    ordering=['id']


def productForm(request):
    products = Product.objects.all()
    context={'products': products }
    if (request.method == "GET"):
        context['productForm'] = ProductForm()
    
    else:
        form = ProductForm(request.POST)
        context['productForm'] = form

        if form.is_valid():
            new_product = Product(
                name= form.cleaned_data['name'],
                price= form.cleaned_data['price'],
                category= form.cleaned_data['category'],
                description= form.cleaned_data['description'],
            )
            new_product.save()

            messages.success(request, 'El producto fue creado con éxito')

            return redirect('index')

    return render(request, 'web/productForm.html', context)

# def clients(request):
#     clients = Client.objects.all().order_by('id')
#     context={
#         'clients': clients,
#     }
#     return render(request, 'web/clients.html', context)

# 'products': [
#     {'name': 'Classic Burger', 'price': 50.0, 'category': 'main', 'description': 'A classic beef burger with lettuce, tomato, and cheese.'},
#     {'name': 'Cheeseburger', 'price': 55.0, 'category': 'main', 'description': 'Juicy beef patty topped with melted cheese, lettuce, and tomato.'},
#     {'name': 'Double Burger', 'price': 70.0, 'category': 'main', 'description': 'Double beef patties with double cheese, lettuce, and tomato.'},
#     {'name': 'French Fries', 'price': 30.0, 'category': 'side', 'description': 'Crispy golden fries served with a side of ketchup.'},
#     {'name': 'Onion Rings', 'price': 35.0, 'category': 'side', 'description': 'Crispy battered onion rings served with a side of ranch.'},
#     {'name': 'Chicken Nuggets', 'price': 40.0, 'category': 'side', 'description': 'Crispy chicken nuggets served with a choice of dipping sauce.'},
#     {'name': 'Hot Dog', 'price': 25.0, 'category': 'main', 'description': 'Classic hot dog with ketchup, mustard, and relish.'},
#     {'name': 'Chicken Sandwich', 'price': 60.0, 'category': 'main', 'description': 'Grilled chicken sandwich with lettuce, tomato, and mayo.'},
#     {'name': 'Caesar Salad', 'price': 45.0, 'category': 'salad', 'description': 'Crisp romaine lettuce with Caesar dressing, croutons, and Parmesan cheese.'},
#     {'name': 'Vanilla Milkshake', 'price': 40.0, 'category': 'dessert', 'description': 'Creamy vanilla milkshake topped with whipped cream.'},
#     {'name': 'Chocolate Milkshake', 'price': 40.0, 'category': 'dessert', 'description': 'Rich chocolate milkshake topped with whipped cream.'},
#     {'name': 'Strawberry Milkshake', 'price': 40.0, 'category': 'dessert', 'description': 'Sweet strawberry milkshake topped with whipped cream.'},
#     {'name': 'Cola Drink', 'price': 20.0, 'category': 'drink', 'description': 'Refreshing cola served chilled.'},
#     {'name': 'Orange Soda', 'price': 20.0, 'category': 'drink', 'description': 'Citrusy orange soda served chilled.'},
#     {'name': 'Mineral Water', 'price': 15.0, 'category': 'drink', 'description': 'Bottled mineral water served chilled.'},
# ]