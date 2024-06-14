from django import forms
from django.core.exceptions import ValidationError
from .models import Client, Product, Order
import re

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['products', 'client']
        widgets = {
            'products': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['products'].queryset = Product.objects.all()



class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    lastname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}))
    dni = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DNI'}))

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["name"]

    def clean_lastname(self):
        lastname = self.cleaned_data["lastname"]
        if not re.match(r'^[A-Za-z\s]+$', lastname):
            raise ValidationError("El apellido debe estar compuesto solo por letras.")
        
        return self.cleaned_data["lastname"]
    
    # def clean_phone(self):
    #     # if not isinstance(self.cleaned_data["phone"], (int, float)):
    #     #     raise ValidationError("El teléfono debe estar compuesto solo por números.")
        
    #     return self.cleaned_data["phone"]
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        clients = Client.objects.all()
        print(clients)
        
        for client in clients:
            if email == client.email:
                raise ValidationError("El email ya fue ingresado")

        return self.cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del plato', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Precio', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': 'Descripción', 'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValidationError("El nombre solo puede estar compuesto por letras y espacios")
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        products = Product.objects.all()

        for product in products:
            if name == product.name:
                raise ValidationError("El producto ya fue ingresado")

        return cleaned_data