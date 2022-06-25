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

    def customize_row(self, row, obj):
        # Customize vehicle column.
        if obj.year and obj.make and obj.model and obj.trim:
            row['year'] = f'{obj.year} {obj.make} {obj.model} {obj.trim}'
        else:
            row['custom_vehicle'] = 'Unknown'

        # Customize VIN column. Shorten VIN to last 6 when on a small viewport.
        if obj.vin:
            row['vin'] = f'<div class="inline d-none d-sm-block" style="float: left;">{obj.vin[:-6]}</div>{obj.vin[-6:]}'
        else:
            row['vin'] = 'Unknown'

        if obj.mileage:
            row['mileage'] = f'{intcomma(obj.mileage)}{obj.mileage_units}'
        else:
            row['mileage'] = 'Unknown'

        if obj.purchaseorder:
            po = obj.purchaseorder
            row['purchase_date'] = f'{(datetime.date.today() - obj.purchaseorder.purchase_date).days}'
        else:
            row['purchase_date'] = 'Unknown'
