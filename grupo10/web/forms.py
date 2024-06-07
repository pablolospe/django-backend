from django import forms
from django.core.exceptions import ValidationError
from .models import Client, Product
import re

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
    
    def clean_phone(self):
        # if not isinstance(self.cleaned_data["phone"], (int, float)):
        #     raise ValidationError("El teléfono debe estar compuesto solo por números.")
        
        return self.cleaned_data["phone"]
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        clients = Client.objects.all()
        print(clients)
        
        for client in clients:
            if email == client.email:
                raise ValidationError("El email ya fue ingresado")

        return self.cleaned_data

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre del plato'}))
    price = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Precio'}))
    category = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Categoría'}))
    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["name"]
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        products = Product.objects.all()
        
        for product in products:
            if name == product.name:
                raise ValidationError("El producto ya fue ingresado")

        return self.cleaned_data