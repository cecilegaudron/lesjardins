# Generated by Django 3.2 on 2023-07-17 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20230704_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'ordering': ('-favourite',)},
        ),
    ]
