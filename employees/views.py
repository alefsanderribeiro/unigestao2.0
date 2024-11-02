from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'employees/home.html'


__all__ = ['HomeView']  # Inclua aqui as views que deseja importar
