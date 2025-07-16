from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeUpdatedDeleteAPIView

urlpatterns = [
    path(
        'emps/',
        EmployeeListCreateAPIView.as_view(),
        name='employee-list-create'
    ),
    path(
        'emp/<int:pk>/',
        EmployeeUpdatedDeleteAPIView.as_view(),
        name='employee-update-delete'
    ),
]
