# Generated by Django 4.2.3 on 2023-07-19 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_mena_alter_product_nazev_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='product_ids',
            new_name='products_ids',
        ),
    ]