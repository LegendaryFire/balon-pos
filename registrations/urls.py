from django.urls import path
from registrations import views, tables

app_name = 'registrations'
urlpatterns = [
    path('tables/registrations/outstanding/', tables.OutstandingRegistrationTableView.as_view(), name="tableOutstanding"),
    path('', views.view_registrations, name='viewOverview'),
]
