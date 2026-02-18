from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Specialite, Service, Medecin

# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialites'] = Specialite.objects.all()  # récupère toutes les spécialités
        return context
    
class SpecialitesView(ListView):
    model = Specialite.objects.all()
    template_name = 'main/acceuil_spe.html'
    context_object_name = 'specialites'
    
class ServicesView(ListView):
    model = Service
    template_name = 'main/services.html'
    context_object_name = 'services'
    
class ServiceDetailView(TemplateView):
    template_name = 'main/service_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_id = self.kwargs.get('pk')
        context['service'] = Service.objects.get(id=service_id)
        return context
class MedecinsView(ListView):
    model = Medecin
    template_name = 'main/medecins.html'
    context_object_name = 'medecins'