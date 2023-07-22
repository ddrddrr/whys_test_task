# Generated by Django 4.2.3 on 2023-07-19 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0003_rename_hodnota_atributu_id_attribute_hodnota_atributu'),
        ('products', '0006_alter_catalog_attributes_ids_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='attributes_ids',
            field=models.ManyToManyField(blank=True, to='attributes.attribute'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='products_ids',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
    ]