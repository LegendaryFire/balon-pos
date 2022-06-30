from django.shortcuts import render
from registrations.models import Registration


def build_outstanding():
    initial_queryset = Registration.objects.filter(date_requested__isnull=True)
    data = {}
    for registration in initial_queryset:
        customer = registration.sales_order.purchaser
        if customer not in data:
            data[str(customer)] = customer.pk
    return data


def view_registrations(request):
    customer_data = build_outstanding()

    context = {
        'customer_data': customer_data,
    }
    return render(request, "registrations/overview.html", context)
