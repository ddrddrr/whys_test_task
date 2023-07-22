# Generated by Django 4.2.3 on 2023-07-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_obrazek_id_catalog_obrazek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mena',
            field=models.CharField(blank=True, choices=[('CZK', 'Czech Crown'), ('EUR', 'Euro'), ('USD', 'US Dollar'), ('GBP', 'British Pound')], max_length=3, verbose_name='Mena'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nazev',
            field=models.CharField(blank=True, max_length=200, verbose_name='Nazev'),
        ),
        migrations.AlterField(
            model_name='product',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Publikovano dne'),
        ),
    ]