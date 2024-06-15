from django.db import models
from grupo10 import settings

class Client(models.Model):
    # name = models.CharField(max_length=100, verbose_name="Nombre")
    # lastname = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(max_length=100, verbose_name="Email")
    phone = models.CharField(max_length=100, verbose_name="Teléfono")
    dni = models.CharField(max_length=100, verbose_name="DNI")
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | dni:{self.dni}"

class Product(models.Model):
    class CategoryChoices(models.TextChoices):
        MAIN = 'MAIN', 'Principal'
        SIDE = 'SIDE', 'Acompañamiento'
        DESSERT = 'DESRT', 'Postre'
        SALAD = 'SALAD', 'Ensalada'
        DRINK = 'DRINK', 'Bebida'

    name = models.CharField(max_length=100, verbose_name="Nombre")
    price = models.FloatField(max_length=100, verbose_name="Precio")
    category = models.CharField(
        max_length=5,
        choices=CategoryChoices.choices,
        verbose_name="Categoría"
    )
    description = models.CharField(max_length=100, verbose_name="Descripción")

    def __str__(self):
        return f"{self.name} price:{self.price} category:{self.category}"
    
class Order(models.Model):
    date = models.DateField(verbose_name="Fecha", auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    products = models.ManyToManyField(Product, verbose_name="Productos")

    def __str__(self):
        return f"{self.date} client:{self.client.name} {self.client.lastname} productos:{self.products.all()}"