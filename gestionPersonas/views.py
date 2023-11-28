from django.shortcuts import render
from django.http import JsonResponse

from .serializers import PersonaSerializers
from .models import Persona
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def vistaPersona(request):
    persona = {
        'id': 1234,
        'nombre': 'Silvester',
        'apellido': 'Stallone',
        'email': 'silvester@gmail.com',
        'sueldo': 10000
    }
    return JsonResponse(persona)


#Usamos el decorador para saber el metodo utilizado
@api_view(['GET'])
def listaPersona(request):
    if request.method == 'GET':
        personas = Persona.objects.all()
        serializer = PersonaSerializers(personas, many= True)
        return Response(serializer.data)