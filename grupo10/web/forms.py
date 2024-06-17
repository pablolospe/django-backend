from django import forms
from django.core.exceptions import ValidationError
from .models import Client, Product, Order
from django.contrib.auth.models import User
import re

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['products']
        widgets = {
            'products': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['products'].queryset = Product.objects.all()

    def render_products(self):
        products_html = '<table class="table">'
        products_html += '<tr><th></th><th>Producto</th><th>Precio</th></tr>'
        for product in self.fields['products'].queryset:
            formatted_price = f'{product.price:.2f}'
            products_html += f'<tr>'
            products_html += f'<td><input type="checkbox" name="products" value="{product.id}"></td>'
            products_html += f'<td>{product.name}</td>'
            products_html += f'<td>{formatted_price}</td>'
            # products_html += f'<td>{product.category}</td>'
            products_html += f'</tr>'
        products_html += '</table>'
        return products_html

class ClientForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Usuario'})
    )
    first_name = forms.CharField(
        max_length=30, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        max_length=30, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Apellido'})
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Password'})
    )
    phone = forms.CharField(
        max_length=15, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    dni = forms.CharField(
        max_length=20, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'DNI'})
    )

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'dni', 'password', 'confirm_password']


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")
        clients = Client.objects.all()
        users = User.objects.all()

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las constraseñas no coinciden")
        
        for client in clients:
            if email == client.email:
                raise ValidationError("El email ya fue ingresado")
        
        for user in users:
            if username == user.username:
                raise ValidationError("El usuario ya fue ingresado")

        return self.cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not re.match(r'^[A-Za-z\s]+$', first_name):
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not re.match(r'^[A-Za-z\s]+$', last_name):
            raise ValidationError("El apellido debe estar compuesto solo por letras.")
        
        return self.cleaned_data["last_name"]

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