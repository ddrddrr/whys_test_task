# Generated by Django 4.2.3 on 2023-07-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0008_remove_attribute_user_defined_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='user_defined_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributename',
            name='user_defined_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='user_defined_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
