from django.urls import path
from . import views
urlpatterns = [
    path("create_appointment/", views.create_appointment, name='create_appointment'),
    path("view_appointment/", views.view_appointment, name="view_appointment"),
    path("list_all_appointments/", views.list_all_appointments, name="list_all_appointments"),
    path("update_appointment/<int:id>", views.update_appointments, name="update_appointment"),
    path("delete_appointment/<int:id>",views.delete_appointment, name = "delete_appointment")
    
]
