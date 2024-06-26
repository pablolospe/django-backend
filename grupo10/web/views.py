from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Product, Client, Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    context={}
    return render(request, 'web/index.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, 'Sessión cerrada con éxito')
    return redirect('index')

def clientForm(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    
    if request.method == "GET":
        context['clientForm'] = ClientForm()
    else:
        form = ClientForm(request.POST)
        context['clientForm'] = form

        if form.is_valid():
            user = User(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],  # Asigna un username, por ejemplo el dni
                email=form.cleaned_data['email']  # Asegúrate de asignar el email también
            )
            user.set_password(form.cleaned_data['password'])
            user.save()

            client = Client(
                user=user,
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                dni=form.cleaned_data['dni'],
            )
            client.save()

            messages.success(request, 'El cliente fue dado de alta con éxito')
            return redirect('index')

    return render(request, 'web/clientForm.html', context)


def menu(request):
    products = Product.objects.all().order_by('id')
    context = {
        'products': products
    }
    return render(request, 'web/menu.html', context)

class ClientListView(LoginRequiredMixin, ListView):
    model=Client
    context_object_name='clients'
    template_name='web/clients.html'
    ordering=['id']

class OrderListView(LoginRequiredMixin, ListView):
    model=Order
    context_object_name='orders'
    template_name='web/orderList.html'
    # ordering=['-id']

    def get_queryset(self):
        user = self.request.user
        orders = Order.objects.filter(client__user=user).order_by('-id')
        for order in orders:
            order.total_price = sum(product.price for product in order.products.all())
        return orders

@login_required
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

def productDetail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'web/productDetail.html', context)    

@login_required
def productEdit(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'El producto fue actualizado con éxito')
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'productForm': form,
        'product': product
    }
    return render(request, 'web/productEdit.html', context)

@login_required
def productDelete(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'El producto fue eliminado con éxito')
        return redirect('index')

    context = {
        'product': product
    }
    return render(request, 'web/productDelete.html', context)


def orderForm(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = request.user.client  # Asume que el usuario tiene un objeto cliente asociado
            order.save()
            form.save_m2m()  # Guarda las relaciones many-to-many
            messages.success(request, 'Pedido realizado con éxito')
            return redirect('index')
    else:
        form = OrderForm()

    return render(request, 'web/orderForm.html', {'form': form})






# 'products': [
#     {'name': 'Classic Burger', 'price': 50.0, 'category': 'MAIN', 'description': 'A classic beef burger with lettuce, tomato, and cheese.'},
#     {'name': 'Cheeseburger', 'price': 55.0, 'category': 'MAIN', 'description': 'Juicy beef patty topped with melted cheese, lettuce, and tomato.'},
#     {'name': 'Double Burger', 'price': 70.0, 'category': 'MAIN', 'description': 'Double beef patties with double cheese, lettuce, and tomato.'},
#     {'name': 'French Fries', 'price': 30.0, 'category': 'SIDE', 'description': 'Crispy golden fries served with a side of ketchup.'},
#     {'name': 'Onion Rings', 'price': 35.0, 'category': 'SIDE', 'description': 'Crispy battered onion rings served with a side of ranch.'},
#     {'name': 'Chicken Nuggets', 'price': 40.0, 'category': 'SIDE', 'description': 'Crispy chicken nuggets served with a choice of dipping sauce.'},
#     {'name': 'Hot Dog', 'price': 25.0, 'category': 'MAIN', 'description': 'Classic hot dog with ketchup, mustard, and relish.'},
#     {'name': 'Chicken Sandwich', 'price': 60.0, 'category': 'MAIN', 'description': 'Grilled chicken sandwich with lettuce, tomato, and mayo.'},
#     {'name': 'Caesar Salad', 'price': 45.0, 'category': 'SALAD', 'description': 'Crisp romaine lettuce with Caesar dressing, croutons, and Parmesan cheese.'},
#     {'name': 'Vanilla Milkshake', 'price': 40.0, 'category': 'DESRT', 'description': 'Creamy vanilla milkshake topped with whipped cream.'},
#     {'name': 'Chocolate Milkshake', 'price': 40.0, 'category': 'DESRT', 'description': 'Rich chocolate milkshake topped with whipped cream.'},
#     {'name': 'Strawberry Milkshake', 'price': 40.0, 'category': 'DESRT', 'description': 'Sweet strawberry milkshake topped with whipped cream.'},
#     {'name': 'Cola Drink', 'price': 20.0, 'category': 'DRIN', 'description': 'Refreshing cola served chilled.'},
#     {'name': 'Orange Soda', 'price': 20.0, 'category': 'DRIN', 'description': 'Citrusy orange soda served chilled.'},
#     {'name': 'Mineral Water', 'price': 15.0, 'category': 'DRIN', 'description': 'Bottled mineral water served chilled.'},
# ]