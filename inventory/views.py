from django.contrib import messages
from django.shortcuts import render, redirect
from inventory.forms import VehicleForm
from sales.forms import PurchaseForm, SaleForm


def view_inventory(request):
    context = {}
    return render(request, 'inventory/overview.html', context)


def view_vehicle(request):
    vehicle_form = VehicleForm(request.POST or None, prefix="vehicle")
    purchase_form = PurchaseForm(request.POST or None, prefix="purchase")
    sales_form = SaleForm(request.POST or None, prefix="sale")

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
    purchase_order = purchase_form.save(commit=False)

    if purchase_form.has_changed():
        # Set the sales person associated with this purchase order if not already set.
        if purchase_order.sales_person_id is None:
            purchase_order.sales_person = request.user

        if purchase_order.vehicle_id is None:
            purchase_order.vehicle = vehicle

        purchase_order.save()

    messages.success(request, 'fuck yeah murica!')
    return redirect('inventory:overview')

