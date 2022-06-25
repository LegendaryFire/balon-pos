from django.http import HttpResponse
from django.shortcuts import render
from inventory.forms import VehicleForm
from inventory.models import Vehicle
from sales.forms import PurchaseForm


def view_inventory(request):
    context = {}
    return render(request, 'inventory/overview.html', context)


def view_vehicle(request):
    context = {
        'vehicle_form': VehicleForm(),
        'purchase_form': PurchaseForm(),
    }
    return render(request, 'inventory/vehicle.html', context)
