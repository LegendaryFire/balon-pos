from django.urls import path
from inventory import views


app_name = 'inventory'
urlpatterns = [
    path('', views.view_inventory, name='overview')
]
