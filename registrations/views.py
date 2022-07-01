from datetime import date
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from registrations.forms import RegistrationRequestForm, RegistrationReceiveForm
from registrations.models import Registration


def mark_requested(pks):
    """
    A function to mark registrations requested as of the current date.
    :param pks: Either a string or integer with a single primary key, or a list of them.
    :return: Returns none.
    """
    if type(pks) in (str, int):
        pks = [pks, ]

    for pk in pks:
        reg = get_object_or_404(Registration, pk=int(pk))
        reg.date_requested = date.today()
        reg.save()


def mark_unrequested(pks):
    """
    A function to mark registrations unrequested.
    :param pks: Either a string or integer with a single primary key, or a list of them.
    :return: Returns none.
    """
    if type(pks) in (str, int):
        pks = [pks, ]

    for pk in pks:
        reg = get_object_or_404(Registration, pk=int(pk))
        reg.date_requested = None
        reg.save()


def mark_received(pks):
    """
    A function to mark registrations received as of the current date.
    :param pks: Either a string or integer with a single primary key, or a list of them.
    :return: Returns none.
    """
    if type(pks) in (str, int):
        pks = [pks, ]

    for pk in pks:
        reg = get_object_or_404(Registration, pk=int(pk))
        reg.date_received = date.today()
        reg.save()


def mark_unreceived(pks):
    """
    A function to mark registrations unreceived.
    :param pks: Either a string or integer with a single primary key, or a list of them.
    :return: Returns none.
    """
    if type(pks) in (str, int):
        pks = [pks, ]

    for pk in pks:
        reg = get_object_or_404(Registration, pk=int(pk))
        reg.date_received = None
        reg.save()


def action_mark_requested(request, pk):
    """
    A view to mark a registration as requested.
    :param request: The request.
    :param pk: The primary key of the registration to mark requested.
    :return: Returns a redirect to the registration overview page.
    """
    mark_requested(pk)
    messages.success(request, 'Registration marked as requested successfully.')
    return redirect('registrations:viewOverview')  # Redirect to the overview page.


def action_mark_unrequested(request, pk):
    """
    A view to mark a registration as unrequested.
    :param request: The request.
    :param pk: The primary key of the registration to mark unrequested.
    :return: Returns a redirect to the registration overview page.
    """
    mark_unrequested(pk)
    messages.success(request, 'Registration marked as unrequested successfully.')
    return redirect('registrations:viewOverview')  # Redirect to the overview page.


def action_mark_received(request, pk):
    """
    A view to mark a registration as received.
    :param request: The request.
    :param pk: The primary key of the registration to mark received.
    :return: Returns a redirect to the registration overview page.
    """
    mark_received(pk)
    messages.success(request, 'Registration marked as received successfully.')
    return redirect('registrations:viewOverview')  # Redirect to the overview page.


def action_mark_unreceived(request, pk):
    """
    A view to mark a registration as unreceived.
    :param request: The request.
    :param pk: The primary key of the registration to mark unreceived.
    :return: Returns a redirect to the registration overview page.
    """
    mark_unreceived(pk)
    messages.success(request, 'Registration marked as unreceived successfully.')
    return redirect('registrations:viewOverview')  # Redirect to the overview page.


def send_registration_request(pks):
    """
    Send bill of sales for registrations.
    :param pks: Either a string or integer with a single primary key, or a list of them.
    :return: Returns none.
    """
    if arg_type := type(pks) is (str or int):
        pks = [pks, ]

    for pk in pks:
        reg = get_object_or_404(Registration, pk=int(pk))
        # TODO: Generate bill of sales for registrations and send to specified email address.


def build_outstanding():
    initial_queryset = Registration.objects.filter(date_received__isnull=True)
    data = {}
    for registration in initial_queryset:
        customer = registration.sales_order.purchaser
        if customer not in data:
            data[str(customer)] = {
                'pk': customer.pk,
                'request_form': RegistrationRequestForm(customer.pk),
                'receive_form': RegistrationReceiveForm(customer.pk),
            }
    return data


def get_request_json(request, customer_id):
    """
    Gets a JSON response of non-requested registrations for a given customer.
    :param request: The HTTP request.
    :param customer_id: The customer ID.
    :return: Returns a JSON response for Select2 heavy widgets.
    """
    initial_queryset = Registration.objects.filter(
        date_received__isnull=True,
        sales_order__purchaser_id=customer_id,
    )

    data = {
        'results': []
    }

    for result in initial_queryset:
        data['results'].append({
            'text': str(result.sales_order.vehicle),
            'id': result.pk,
        })

    return JsonResponse(data)


def view_registrations(request):
    if request.method == "POST":
        if action := request.POST.get('action'):
            if action == 'request':
                pks = request.POST.getlist('select_request_2')
                send_registration_request(pks)
                mark_requested(pks)
                messages.success(request, f'Registrations requested successfully.')
            elif action == 'receive':
                pks = request.POST.getlist('select_receive_2')
                mark_received(pks)
                messages.success(request, f'Registrations received successfully.')

    customer_data = build_outstanding()

    context = {
        'customer_data': customer_data,
    }
    return render(request, "registrations/overview.html", context)
