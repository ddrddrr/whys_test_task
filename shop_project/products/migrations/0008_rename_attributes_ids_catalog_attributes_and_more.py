# Generated by Django 4.2.3 on 2023-07-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_catalog_attributes_ids_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='attributes_ids',
            new_name='attributes',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='obrazek',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='products_ids',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='obrazek',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='nazev',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cena',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mena',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nazev',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='nazev',
        ),
        migrations.AddField(
            model_name='catalog',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, choices=[('CZK', 'Czech Crown'), ('EUR', 'Euro'), ('USD', 'US Dollar'), ('GBP', 'British Pound')], max_length=3),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
