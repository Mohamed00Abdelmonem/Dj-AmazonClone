# Generated by Django 4.2.4 on 2024-02-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_cart_status_alter_order_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('InProgress', 'InProgress')], max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='H8MS0TW3', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Recieved', 'Recieved'), ('Delivered', 'Delivered'), ('Shipped', 'Shipped'), ('Processed', 'Processed')], default='Recieved', max_length=10),
        ),
    ]