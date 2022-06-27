from django.urls import path
from customers import views

app_name = 'customers'
urlpatterns = [
    path('ajax/add-customer/', views.ajax_add_customer, name='ajaxAddCustomer'),
]
