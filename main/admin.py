from django.contrib import admin
from .models import Specialite, Service

# Register your models here.
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image')
    search_fields = ('nom',)
    
admin.site.register(Specialite, SpecialiteAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'created_at')
    search_fields = ('nom',)
admin.site.register(Service, ServiceAdmin)