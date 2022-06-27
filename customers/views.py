from django.http import HttpResponse
from django.shortcuts import render
from customers.forms import CustomerForm


def ajax_add_customer(request):
    customer_form = CustomerForm(request.POST or None)
    if request.method == "POST" and customer_form.is_valid():
        customer_form.save()
        return HttpResponse(200)
