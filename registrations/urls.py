from django.urls import path
from registrations import views, tables

app_name = 'registrations'
urlpatterns = [
    path('action/mark/requested/<int:pk>/', views.action_mark_requested, name='actionMarkRequested'),
    path('action/mark/unrequested/<int:pk>/', views.action_mark_unrequested, name='actionMarkUnrequested'),
    path('action/mark/received/<int:pk>/', views.action_mark_received, name='actionMarkReceived'),
    path('action/mark/unreceived/<int:pk>/', views.action_mark_unreceived, name='actionMarkUnreceived'),
    path('tables/outstanding/', tables.OutstandingRegistrationTableView.as_view(), name="tableOutstanding"),
    path('select2/outstanding/<int:customer_id>/', views.get_request_json, name='selectRequest'),
    path('', views.view_registrations, name='viewOverview'),
]
