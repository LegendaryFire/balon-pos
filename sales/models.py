from django.db import models
from datetime import date


class PurchaseOrder(models.Model):
    purchase_number = models.BigAutoField(primary_key=True, verbose_name="Purchase Number")
    seller = models.ForeignKey('customers.Customer', on_delete=models.RESTRICT, verbose_name="Seller")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Purchase Price")
    pst = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, verbose_name="PST Paid")
    gst = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, verbose_name="GST Paid")
    method = models.CharField(max_length=64, verbose_name="Payment Method")
    notes = models.CharField(max_length=64, verbose_name="Payment Notes")
    purchase_date = models.DateField(default=date.today, verbose_name="Purchase Date")
    asking_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, verbose_name="Asking Price")
    bill_of_sale = models.ImageField(null=True, blank=True, verbose_name="Bill of Sale")
    sales_person = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, verbose_name="Sales Person")
    vehicle = models.OneToOneField('inventory.Vehicle', on_delete=models.CASCADE, verbose_name="Vehicle")


class SalesOrder(models.Model):
    sale_number = models.BigAutoField(primary_key=True, verbose_name="Sale Number")
    purchaser = models.ForeignKey('customers.Customer', on_delete=models.RESTRICT, null=True, blank=False, verbose_name="Purchaser")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Sale Price")
    pst = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, verbose_name="PST Charged")
    gst = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, verbose_name="GST Charged")
    method = models.CharField(max_length=64, null=True, blank=True, verbose_name="Payment Method")
    notes = models.CharField(max_length=64, null=True, blank=True, verbose_name="Payment Notes")
    sale_mileage = models.IntegerField(null=False, blank=False, default=0, verbose_name='Sale Mileage')
    sale_date = models.DateField(default=date.today, verbose_name="Date Sold")
    paid_date = models.DateField(default=None, null=True, blank=True, verbose_name="Date Paid")
    bill_of_sale = models.ImageField(null=True, blank=True, verbose_name="Bill of Sale")
    sales_person = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, verbose_name="Sales Person")
    vehicle = models.OneToOneField('inventory.Vehicle', on_delete=models.CASCADE, verbose_name="Vehicle")
