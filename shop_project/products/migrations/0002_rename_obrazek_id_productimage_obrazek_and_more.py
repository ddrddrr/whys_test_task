# Generated by Django 4.2.3 on 2023-07-17 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='obrazek_id',
            new_name='obrazek',
        ),
        migrations.AlterField(
            model_name='catalog',
            name='obrazek_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.image'),
        ),
    ]