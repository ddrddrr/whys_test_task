# Generated by Django 4.2.3 on 2023-07-24 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0010_remove_attribute_user_defined_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='_actual_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='attributename',
            name='_actual_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attributename',
            name='id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='_actual_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='id',
            field=models.IntegerField(unique=True),
        ),
    ]
