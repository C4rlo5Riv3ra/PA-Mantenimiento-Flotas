from rest_framework import serializers
from .models import (
    Persona, Usuario, TipoVehiculo, Vehiculo, Conductor, Asignacion,
    TipoMantenimiento, Mantenimiento, AlertaMantenimiento,
    ServicioMantenimiento, DetalleMantenimiento
)

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = '__all__'

class TipoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMantenimiento
        fields = '__all__'

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class AlertaMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertaMantenimiento
        fields = '__all__'

class ServicioMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioMantenimiento
        fields = '__all__'

class DetalleMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleMantenimiento
        fields = '__all__'
