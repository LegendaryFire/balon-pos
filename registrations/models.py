from django.db import models


class Registration(models.Model):
    id = models.BigAutoField(primary_key=True)
    charged = models.DecimalField(max_digits=6, default=0.00, decimal_places=2, verbose_name="Charged")
    date_requested = models.DateField(default=None, null=True, blank=True, verbose_name="Date Requested")
    date_received = models.DateField(default=None, null=True, blank=True, verbose_name="Date Received")
    scan = models.ImageField(null=True, blank=True, verbose_name="Registration", upload_to="registrations/")
    sales_order = models.OneToOneField('sales.SalesOrder', on_delete=models.CASCADE, verbose_name="Sales Order")

    def __str__(self):
        if hasattr(self, 'sales_order'):
            vehicle = self.sales_order.vehicle
            return f'{vehicle.year} {vehicle.make} {vehicle.model} {vehicle.trim} - {vehicle.vin[-6:]}'
