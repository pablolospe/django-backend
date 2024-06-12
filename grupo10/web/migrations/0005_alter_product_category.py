# Generated by Django 4.2.13 on 2024-06-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MAIN', 'Principal'), ('SIDE', 'Acompañamiento'), ('DESRT', 'Postre'), ('SALAD', 'Ensalada'), ('DRINK', 'Bebida')], max_length=5, verbose_name='Categoría'),
        ),
    ]