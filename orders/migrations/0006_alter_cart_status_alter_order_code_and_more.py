# Generated by Django 4.2.4 on 2023-10-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_cart_coupon_alter_cart_status_alter_order_code'),
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
            field=models.CharField(default='Y8ONS26A', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processed', 'Processed'), ('Recieved', 'Recieved'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Recieved', max_length=10),
        ),
    ]
