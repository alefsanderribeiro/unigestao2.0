from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView
from django.http import HttpResponse
from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/list_employees.html'
    context_object_name = 'employees'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/partial/employee_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if self.request.headers.get('Hx-Request'):
            form.save()
            return HttpResponse('Item criado com sucesso!', status=201)
        return super().form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/partial/employee_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if self.request.headers.get('Hx-Request'):
            form.save()
            return HttpResponse('Funcionário atualizado com sucesso!', status=200)
        return super().form_valid(form)
