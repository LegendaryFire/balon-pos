from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve
from customers.forms import CustomerForm
from inventory.forms import VehicleForm
from inventory.models import Vehicle
from sales.forms import PurchaseForm, SaleForm


def view_inventory(request):
    context = {}
    return render(request, 'inventory/overview.html', context)


def view_vehicle(request, stock=None):
    class URLNames:
        """
        Enumerator class used to distinguish the purpose of the vehicle view.
        """
        ADD = 'add_vehicle'
        EDIT = 'edit_vehicle'
        SELL = 'sell_vehicle'

    # Handle the create customer proportion of the vehicle page.
    customer_form = CustomerForm(request.POST or None)
    if request.method == "POST" and customer_form.is_valid():
        customer_form.save()
        return HttpResponse(200)

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

    # Check to see what our purpose is. Are we here to add, edit or sell a vehicle.
    purpose = resolve(request.path_info).url_name
    match purpose:
        case URLNames.EDIT:
            # Disable all sale form fields.
            for field in sales_form.fields:
                sales_form.fields[field].disabled = True
        case URLNames.SELL:
            # Disable all vehicle & purchase form fields.
            for field in vehicle_form.fields:
                vehicle_form.fields[field].disabled = True
            for field in purchase_form.fields:
                purchase_form.fields[field].disabled = True

    context = {
        'vehicle_form': vehicle_form,
        'purchase_form': purchase_form,
        'sales_form': sales_form,
        'customer_form': customer_form,
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

    match purpose:
        case URLNames.ADD:
            messages.success(
                request,
                f'{vehicle.year} {vehicle.make} {vehicle.model} {vehicle.trim} - {vehicle.vin[-6:]} added.'
            )
        case URLNames.EDIT:
            messages.success(
                request,
                f'Changes to {vehicle.year} {vehicle.make} {vehicle.model} {vehicle.trim} - {vehicle.vin[-6:]} saved.'
            )
        case URLNames.SELL:
            messages.success(
                request,
                f'{vehicle.year} {vehicle.make} {vehicle.model} {vehicle.trim} - {vehicle.vin[-6:]} sold to {sales_order.purchaser.first_name} {sales_order.purchaser.last_name}.'
            )
    return redirect('inventory:overview')
