from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    sueldo = models.IntegerField()
    
    def __str__(self):
        return str(self.id) + " " + self.nombre + " Su sueldo es:  " + str(self.sueldo)
    
    
    
    