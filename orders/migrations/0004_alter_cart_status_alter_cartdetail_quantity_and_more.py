# Generated by Django 4.2.4 on 2023-10-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_cart_status_alter_order_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('InProgress', 'InProgress')], max_length=10),
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='DPT3EC0G', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Recieved', 'Recieved'), ('Processed', 'Processed')], max_length=10),
        ),
    ]
