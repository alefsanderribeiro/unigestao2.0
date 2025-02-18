from django.urls import path
from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView

urlpatterns = [
    path('employee_list/', EmployeeListView.as_view(), name='employee-list'),
    path('employee_create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee_update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
]
