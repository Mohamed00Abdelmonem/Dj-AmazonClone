# Generated by Django 4.2.4 on 2024-02-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='7LTK690I', max_length=9),
        ),
    ]
