# Generated by Django 4.0.5 on 2022-06-25 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
        ('inventory', '0003_alter_vehicle_disclosures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='purchase_order',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='sales.purchaseorder', verbose_name='Purchase Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='sales_order',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='sales.salesorder', verbose_name='Sales Order'),
            preserve_default=False,
        ),
    ]