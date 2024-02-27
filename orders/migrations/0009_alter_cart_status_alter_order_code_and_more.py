# Generated by Django 4.2.4 on 2024-02-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('InProgress', 'InProgress'), ('Completed', 'Completed')], max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='21VB5Y2T', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Processed', 'Processed'), ('Recieved', 'Recieved'), ('Shipped', 'Shipped')], default='Recieved', max_length=10),
        ),
    ]