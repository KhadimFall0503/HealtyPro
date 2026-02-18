from django.contrib import admin
from .models import Specialite, Service, Medecin

# Register your models here.
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image')
    search_fields = ('nom',)
    
admin.site.register(Specialite, SpecialiteAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'created_at')
    search_fields = ('nom',)
admin.site.register(Service, ServiceAdmin)

class MedecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'specialite', 'service')
    search_fields = ('nom', 'prenom')
admin.site.register(Medecin, MedecinAdmin)