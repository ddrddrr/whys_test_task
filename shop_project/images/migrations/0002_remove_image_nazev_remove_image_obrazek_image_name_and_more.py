# Generated by Django 4.2.3 on 2023-07-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='nazev',
        ),
        migrations.RemoveField(
            model_name='image',
            name='obrazek',
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='image',
            name='source_url',
            field=models.URLField(default=''),
        ),
    ]
