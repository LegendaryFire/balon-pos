import datetime
from ajax_datatable import AjaxDatatableView
from registrations.models import Registration


class OutstandingRegistrationTableView(AjaxDatatableView):
    model = Registration
    title = 'Registrations'
    show_column_filters = False
    search_values_separator = ' '

    column_defs = [
        {
            'name': 'vehicle',
            'foreign_field': 'sales_order__vehicle',
            'title': 'Vehicle',
            'visible': True,
        }, {
            'name': 'vin',
            'foreign_field': 'sales_order__vehicle__vin',
            'title': 'Purchaser',
            'visible': True,
        }, {
            'name': 'charged',
            'title': 'Price',
            'visible': True,
        }, {
            'name': 'date_requested',
            'title': 'Requested',
            'placeholder': True,
        },
    ]

    def get_initial_queryset(self, request=None):
        if 'customer_number' in request.REQUEST:
            customer_number = int(request.REQUEST.get('customer_number'))
            return Registration.objects.filter(sales_order__purchaser__customer_number=customer_number)

    def customize_row(self, row, obj):
        # Customize vehicle column.
        if obj.sales_order.vehicle:
            vehicle = obj.sales_order.vehicle
            row['vehicle'] = f'{vehicle.year} {vehicle.make} {vehicle.model} {vehicle.trim}'
        else:
            row['vehicle'] = 'Unknown'

        # Customize VIN column. Shorten VIN to last 6 when on a small viewport.
        if obj.sales_order.vehicle.vin:
            row['vin'] = f'<div class="inline d-none d-sm-block" style="float: left;">{obj.sales_order.vehicle.vin[:-8]}</div>{obj.sales_order.vehicle.vin[-8:]}'
        else:
            row['vin'] = 'Unknown'

        # Customize mileage column. Format the integer, and add a unit of measurement.
        if obj.date_requested:
            row['date_requested'] = f'{(datetime.date.today() - obj.date_requested).days} Days'
        else:
            row['date_requested'] = 'Not Requested'

        # Customize the action column. Create a dropdown menu allowing options on the unit.
        row['action'] = f"""
        <div class="dropdown">
            <button class="btn btn-success action" type="button" id="actionDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="mdi mdi-arrow-down" aria-hidden="true"></i>
            </button>
            <ul class="dropdown-menu" aria-labelledby="actionDropdown">
                <li><a class="dropdown-item" href="vehicle/edit/">Edit Vehicle</a></li>
            </ul>
        </div>
        """
