from django.urls import path
from employees.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
