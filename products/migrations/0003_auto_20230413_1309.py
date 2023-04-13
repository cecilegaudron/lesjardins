# Generated by Django 3.2 on 2023-04-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230413_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_kilo',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
