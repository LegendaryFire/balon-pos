from django.http import HttpResponse
from django.shortcuts import render


def view_inventory(request):
    return render(request, 'inventory/overview.html')
