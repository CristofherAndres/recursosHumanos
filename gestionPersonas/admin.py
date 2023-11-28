from django.contrib import admin
from gestionPersonas.models import Persona

class personaAdmin(admin.ModelAdmin):
    list_display = ['nombre','correo','sueldo']
    

admin.site.register(Persona, personaAdmin)