from django.urls import path
from inventory import views, tables

app_name = 'inventory'
urlpatterns = [
    path('tables/inventory', tables.InventoryTableView.as_view(), name="inventory_table"),
    path('', views.view_inventory, name='overview'),
    path('vehicle/add/', views.view_vehicle, name='add_vehicle'),
    path('vehicle/edit/<int:stock>/', views.view_vehicle, name='edit_vehicle'),
    path('vehicle/sell/<int:stock>/', views.view_vehicle, name='sell_vehicle'),
]
