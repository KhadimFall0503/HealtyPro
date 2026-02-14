from django.db import models

# Create your models here.
class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='specialites/')
    
    def __str__(self):
        return self.nom
    
class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    icone_svg = models.TextField(blank=True, null=True)  # Optionnel : code SVG ou nom d'icône
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
