# Generated by Django 3.2 on 2023-07-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20230701_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=4000, verbose_name='Your message*'),
        ),
    ]