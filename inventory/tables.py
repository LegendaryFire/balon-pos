import datetime
from django.contrib.humanize.templatetags.humanize import intcomma
from ajax_datatable.views import AjaxDatatableView
from inventory.models import Vehicle


class InventoryTableView(AjaxDatatableView):
    model = Vehicle
    title = 'Inventory'
    show_column_filters = False
    search_values_separator = ' '

    column_defs = [
        {
            'name': 'year',
            'title': 'Vehicle',
            'visible': True,
        }, {
            'name': 'vin',
            'title': 'VIN',
            'visible': True,
        }, {
            'name': 'mileage',
            'title': 'Mileage',
            'visible': True,
        }, {
            'name': 'purchase_date',
            'foreign_field': 'purchaseorder__purchase_date',
            'title': 'Days',
            'visible': True,
        }, {
            'name': 'action',
            'title': 'Action',
            'placeholder': True,
        }, {
            'name': 'make',
            'searchable': True,
            'orderable': False,
            'visible': False,
        }, {
            'name': 'model',
            'searchable': True,
            'orderable': False,
            'visible': False,
        }, {
            'name': 'trim',
            'searchable': True,
            'orderable': False,
            'visible': False,
        },
    ]

    def get_initial_queryset(self, request=None):
        return Vehicle.objects.filter(salesorder__isnull=True)

    def customize_row(self, row, obj):
        # Customize vehicle column.
        if obj.year and obj.make and obj.model and obj.trim:
            row['year'] = f'{obj.year} {obj.make} {obj.model} {obj.trim}'
        else:
            row['year'] = 'Unknown'

        # Customize VIN column. Shorten VIN to last 6 when on a small viewport.
        if obj.vin:
            row['vin'] = f'<div class="inline d-none d-sm-block" style="float: left;">{obj.vin[:-6]}</div>{obj.vin[-6:]}'
        else:
            row['vin'] = 'Unknown'

        # Customize mileage column. Format the integer, and add a unit of measurement.
        if obj.mileage:
            row['mileage'] = f'{intcomma(obj.mileage)}{obj.mileage_units}'
        else:
            row['mileage'] = 'Unknown'

        # Customize the purchase date column, calculate how many days it's been in inventory.
        if obj.purchaseorder:
            po = obj.purchaseorder
            row['purchase_date'] = f'{(datetime.date.today() - obj.purchaseorder.purchase_date).days}'
        else:
            row['purchase_date'] = 'Unknown'

        # Customize the action column. Create a dropdown menu allowing options on the unit.
        row['action'] = f"""
        <div class="dropdown">
            <button class="btn btn-success action" type="button" id="actionDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="mdi mdi-arrow-down" aria-hidden="true"></i>
            </button>
            <ul class="dropdown-menu" aria-labelledby="actionDropdown">
                <li><a class="dropdown-item" href="vehicle/edit/{obj.stock}">Edit Vehicle</a></li>
                <li><a class="dropdown-item" href="vehicle/sell/{obj.stock}">Sell Vehicle</a></li>
            </ul>
        </div>
        """


class SoldTableView(AjaxDatatableView):
    model = Vehicle
    title = 'Sold Inventory'
    show_column_filters = False
    search_values_separator = ' '

    column_defs = [
        {
            'name': 'year',
            'title': 'Vehicle',
            'visible': True,
        }, {
            'name': 'vin',
            'title': 'VIN',
            'visible': True,
        }, {
            'name': 'purchaser',
            'foreign_field': 'salesorder__purchaser',
            'title': 'Purchaser',
            'searchable': False,
            'orderable': False,
            'visible': True,
        }, {
            'name': 'sale_date',
            'foreign_field': 'salesorder__sale_date',
            'title': 'Sale Date',
            'visible': True,
        }, {
            'name': 'mileage',
            'title': 'Mileage',
            'visible': True,
        }, {
            'name': 'action',
            'title': 'Action',
            'placeholder': True,
        }, {
            'name': 'make',
            'searchable': True,
            'orderable': False,
            'visible': False,
        }, {
            'name': 'model',
            'searchable': True,
            'orderable': False,
            'visible': False,
        }, {
            'name': 'trim',
            'searchable': True,
            'orderable': False,
            'visible': False,
        },
    ]

    def get_initial_queryset(self, request=None):
        return Vehicle.objects.filter(salesorder__isnull=False)

    def customize_row(self, row, obj):
        # Customize vehicle column.
        if obj.year and obj.make and obj.model and obj.trim:
            row['year'] = f'{obj.year} {obj.make} {obj.model} {obj.trim}'
        else:
            row['year'] = 'Unknown'

        # Customize VIN column. Shorten VIN to last 6 when on a small viewport.
        if obj.vin:
            row['vin'] = f'<div class="inline d-none d-sm-block" style="float: left;">{obj.vin[:-6]}</div>{obj.vin[-6:]}'
        else:
            row['vin'] = 'Unknown'

        # Customize mileage column. Format the integer, and add a unit of measurement.
        if obj.mileage:
            row['mileage'] = f'{intcomma(obj.mileage)}{obj.mileage_units}'
        else:
            row['mileage'] = 'Unknown'

        # Customize the action column. Create a dropdown menu allowing options on the unit.
        row['action'] = f"""
        <div class="dropdown">
            <button class="btn btn-success action" type="button" id="actionDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="mdi mdi-arrow-down" aria-hidden="true"></i>
            </button>
            <ul class="dropdown-menu" aria-labelledby="actionDropdown">
                <li><a class="dropdown-item" href="vehicle/edit/{obj.stock}">Edit Vehicle</a></li>
            </ul>
        </div>
        """
