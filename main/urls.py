from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
   
]
