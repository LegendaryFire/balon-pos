from django.shortcuts import render
from inventory.forms import VehicleForm
from sales.forms import PurchaseForm


def view_inventory(request):
    return render(request, 'inventory/overview.html')


def view_vehicle(request):
    context = {
        'vehicle_form': VehicleForm(),
        'purchase_form': PurchaseForm(),
    }
    return render(request, 'inventory/vehicle.html', context)
