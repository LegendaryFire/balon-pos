from django.contrib import admin
from sales.models import PurchaseOrder, SalesOrder

admin.site.register(PurchaseOrder)
admin.site.register(SalesOrder)
