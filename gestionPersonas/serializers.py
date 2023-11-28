from rest_framework import serializers
from gestionPersonas.models import Persona

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'