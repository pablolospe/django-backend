from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True) 
    lastname = forms.CharField(label="Apellido", required=True) 
    phone = forms.IntegerField(label="Teléfono", required=True)
    email = forms.EmailField(label="email", required=True)
    address = forms.CharField(label="Dirección", required=True) 