# Generated by Django 4.2.3 on 2023-07-22 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0004_rename_kod_attributename_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='nazev_atributu',
            new_name='attribute_name',
        ),
        migrations.RenameField(
            model_name='attribute',
            old_name='hodnota_atributu',
            new_name='attribute_value',
        ),
        migrations.RenameField(
            model_name='attributevalue',
            old_name='hodnota',
            new_name='value',
        ),
    ]
