from django import forms
from django.core.exceptions import ValidationError

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    lastname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))

    def clean_name(self):
        if not self.cleaned_data["name"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["name"]

    def clean_lastname(self):
        if not self.cleaned_data["lastname"].isalpha():
            raise ValidationError("El apellido debe estar compuesto solo por letras.")
        
        return self.cleaned_data["lastname"]
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        lastname = cleaned_data.get("lastname")
        
        if name == "Carlos":
            raise ValidationError("El usuario Carlos Lopez ya existe")

        return self.cleaned_data