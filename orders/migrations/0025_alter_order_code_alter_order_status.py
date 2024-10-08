# Generated by Django 4.2.4 on 2024-09-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='16AOA60L', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processed', 'Processed'), ('Delivered', 'Delivered'), ('Recieved', 'Recieved'), ('Shipped', 'Shipped')], default='Recieved', max_length=10),
        ),
    ]
