# Generated by Django 4.2.4 on 2024-03-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='max_quantity',
            field=models.IntegerField(default=100, verbose_name='Max Quantity'),
        ),
    ]
