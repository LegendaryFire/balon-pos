from django.urls import path
from inventory import views, tables

app_name = 'inventory'
urlpatterns = [
    path('tables/inventory', tables.InventoryTableView.as_view(), name="tableInventory"),
    path('', views.view_inventory, name='viewOverview'),
    path('vehicle/add/', views.view_vehicle, name='viewAddVehicle'),
    path('vehicle/edit/<int:stock>/', views.view_vehicle, name='viewEditVehicle'),
    path('vehicle/sell/<int:stock>/', views.view_vehicle, name='viewSellVehicle'),
]
