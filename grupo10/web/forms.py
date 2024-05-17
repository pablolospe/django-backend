from django import forms

# class ClientForm(forms.Form):
#     name = forms.CharField(label="Nombre", required=True) 
#     lastname = forms.CharField(label="Apellido", required=True) 
#     phone = forms.IntegerField(label="Teléfono", required=True)
#     email = forms.EmailField(label="email", required=True)
#     address = forms.CharField(label="Dirección", required=True) 



class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))
