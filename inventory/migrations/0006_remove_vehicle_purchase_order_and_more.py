# Generated by Django 4.0.5 on 2022-06-25 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_vehicle_sales_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='purchase_order',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='sales_order',
        ),
    ]
