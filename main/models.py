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
class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='medecins/')
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
