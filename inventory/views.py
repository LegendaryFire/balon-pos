from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from inventory.forms import VehicleForm
from inventory.models import Vehicle
from sales.forms import PurchaseForm, SaleForm


def view_inventory(request):
    context = {}
    return render(request, 'inventory/overview.html', context)


def view_vehicle(request, stock=None):
    # Check to see if a specific stock number was requested. If so, pull the vehicle data.
    vehicle = None
    purchase_order = None
    sales_order = None

    if stock:
        vehicle = get_object_or_404(Vehicle, pk=stock)
        if hasattr(vehicle, 'purchaseorder'):
            purchase_order = vehicle.purchaseorder
        if hasattr(vehicle, 'salesorder'):
            sales_order = vehicle.salesorder

    vehicle_form = VehicleForm(request.POST or None, instance=vehicle, prefix="vehicle")
    purchase_form = PurchaseForm(request.POST or None, instance=purchase_order, prefix="purchase")
    sales_form = SaleForm(request.POST or None, instance=sales_order, prefix="sale")

    context = {
        'vehicle_form': vehicle_form,
        'purchase_form': purchase_form,
        'sales_form': sales_form,
    }

    if request.method != 'POST':
        return render(request, 'inventory/vehicle.html', context)

    # Make sure the vehicle form is valid.
    if not vehicle_form.is_valid():
        messages.error(request, 'Vehicle information is incorrect or missing.')
        return render(request, "inventory/vehicle.html", context)

    # Make sure the purchase form is valid.
    if not purchase_form.is_valid():
        messages.error(request, 'Purchase information is incorrect or missing.')
        return render(request, "inventory/vehicle.html", context)

    vehicle = vehicle_form.save()

    if purchase_form.has_changed():
        purchase_order = purchase_form.save(commit=False)

        # Associate the sales person with this purchase order if not already set.
        if purchase_order.sales_person_id is None:
            purchase_order.sales_person = request.user

        # Associate the vehicle with the purchase order if not already set.
        if purchase_order.vehicle_id is None:
            purchase_order.vehicle = vehicle

        purchase_order.save()

    if sales_form.has_changed():
        # Make sure sale form is valid.
        if not sales_form.is_valid():
            messages.error(request, 'Sale information is incorrect or missing.')
            return render(request, "inventory/vehicle.html", context)

        sales_order = sales_form.save(commit=False)

        # Associate the sales person with this purchase order if not already set.
        if sales_order.sales_person_id is None:
            sales_order.sales_person = request.user

        # Associate the vehicle with the purchase order if not already set.
        if sales_order.vehicle_id is None:
            sales_order.vehicle = vehicle

        sales_order.save()



    messages.success(request, 'fuck yeah murica!')
    return redirect('inventory:overview')

