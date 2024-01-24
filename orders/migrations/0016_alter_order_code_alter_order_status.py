# Generated by Django 4.2.4 on 2024-01-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_cart_status_alter_order_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='SVF0GLEY', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Recieved', 'Recieved'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Processed', 'Processed')], default='Recieved', max_length=10),
        ),
    ]
