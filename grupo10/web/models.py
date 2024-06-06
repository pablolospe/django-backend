from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    lastname = models.CharField(max_length=100, verbose_name="Apellido")
    phone = models.CharField(max_length=100, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    dni = models.CharField(max_length=100, verbose_name="DNI")

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    price = models.FloatField(max_length=100, verbose_name="Precio")
    category = models.CharField(max_length=100, verbose_name="Categoría")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    
class Order(models.Model):
    date = models.DateField(verbose_name="Fecha", auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    products = models.ManyToManyField(Product, verbose_name="Productos")