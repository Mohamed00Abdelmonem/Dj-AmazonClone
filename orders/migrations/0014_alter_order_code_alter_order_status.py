# Generated by Django 4.2.4 on 2024-01-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_cart_status_alter_order_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='QA3I2MM0', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Shipped', 'Shipped'), ('Processed', 'Processed'), ('Recieved', 'Recieved')], default='Recieved', max_length=10),
        ),
    ]