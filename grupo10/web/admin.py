from django.contrib import admin
from .models import Product, Client, Order

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
