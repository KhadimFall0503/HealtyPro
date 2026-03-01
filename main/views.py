from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Service, Medecin


class IndexView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('-id')[:4]  # 4 services récents
        return context


class ServicesView(ListView):
    model = Service
    template_name = 'main/services.html'
    context_object_name = 'services'
    ordering = ['-id']


class ServiceDetailView(TemplateView):
    template_name = 'main/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_id = self.kwargs.get('pk')
        context['service'] = get_object_or_404(Service, id=service_id)
        return context


class MedecinsView(ListView):
    model = Medecin
    template_name = 'main/medecins.html'
    context_object_name = 'medecins'