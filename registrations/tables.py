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
            'visible': True,
        }, {
            'name': 'action',
            'title': 'Action',
            'searchable': False,
            'orderable': False,
            'placeholder': True,
        }
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

        # Customize date requested column, save the status since we will use it in our action column.
        requested = False
        if obj.date_requested:
            row['date_requested'] = f'{(datetime.date.today() - obj.date_requested).days} Days'
            requested = True
        else:
            row['date_requested'] = 'Not Requested'

        # Customize the action column. Create a dropdown menu allowing options on the registration.
        row['action'] = f"""
        <div class="dropdown">
            <button class="btn btn-success action" type="button" id="actionDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="mdi mdi-arrow-down" aria-hidden="true"></i>
            </button>
            <ul class="dropdown-menu" aria-labelledby="actionDropdown">
                {f'<li><a class="dropdown-item" href="action/mark/requested/{obj.pk}">Mark Requested</a></li>' if not requested else ''}
                <li><a class="dropdown-item" href="action/mark/received/{obj.pk}">Mark Received</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="edit/{obj.pk}">Edit Registration</a></li>
            </ul>
        </div>
        """
