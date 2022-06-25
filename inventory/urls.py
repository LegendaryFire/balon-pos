from django.urls import path
from inventory import views, tables

app_name = 'inventory'
urlpatterns = [
    path('tables/inventory', tables.InventoryTableView.as_view(), name="inventory_table"),
    path('', views.view_inventory, name='overview'),
    path('vehicle/', views.view_vehicle, name='vehicle'),
]
