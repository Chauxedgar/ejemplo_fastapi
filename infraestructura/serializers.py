from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import IncidenciaServidor, NodoServidor


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    # Cambiamos 'url' por 'id'
    fields = ['id', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):

  class Meta:
    model = Group
    # Cambiamos 'url' por 'id'
    fields = ['id', 'name']


# ... el resto de tus serializers (IncidenciaServidorSerializer y NodoServidorSerializer) se mantienen igual ...


class IncidenciaServidorSerializer(serializers.ModelSerializer):
  servidor_nombre = serializers.ReadOnlyField(source='servidor.nombre_host')

  class Meta:
    model = IncidenciaServidor
    fields = [
        'id',
        'servidor',
        'servidor_nombre',
        'titulo',
        'descripcion',
        'severidad',
        'resuelta',
        'fecha_reporte',
    ]
    read_only_fields = ['id', 'fecha_reporte']


class NodoServidorSerializer(serializers.ModelSerializer):
  motor_contenedores_display = serializers.CharField(
      source='get_motor_contenedores_display', read_only=True
  )
  incidencias = IncidenciaServidorSerializer(many=True, read_only=True)

  class Meta:
    model = NodoServidor
    fields = '__all__'