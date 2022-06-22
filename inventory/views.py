from django.shortcuts import render
from inventory.forms import VehicleForm


def view_inventory(request):
    return render(request, 'inventory/overview.html')


def view_vehicle(request):
    context = {
        'vehicle_form': VehicleForm(),
    }
    return render(request, 'inventory/vehicle.html', context)
