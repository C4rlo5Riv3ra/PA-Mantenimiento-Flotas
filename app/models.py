from django.db import models
from proyect.choices import *

# Create your models here.

# Modelo Persona
class Persona(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    doc_identity = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=80)

    class Meta:
        db_table = "persona"
        ordering = ['id']

# Modelo Usuario
class Usuario(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=60, null=False)
    password = models.CharField(max_length=60, null=False)
    id_rol = models.IntegerField(choices=rol)
    id_person = models.ForeignKey(Persona, on_delete=models.RESTRICT, null=False, related_name='usuario')
    state = models.IntegerField(choices=estado_Usuario, default=estado_Usuario.ACTIVO)
    last_date_support = models.DateField(null=True, blank=True)
    next_date_support = models.DateField(null=True, blank=True)


    class Meta:
        db_table = "usuario"
        ordering = ['id']

# Modelo Tipo Vehiculo
class TipoVehiculo(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'tipo_vehiculo'
        ordering = ['id']

# Modelo Vehiculo
class Vehiculo(models.Model):
    id = models.UUIDField(primary_key=True)
    placa = models.CharField(max_length=15, unique=True)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField()
    id_tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.RESTRICT, null=False, related_name='tipo_vehiculo')
    state = models.IntegerField(choices=estado_Vehiculo, default=estado_Vehiculo.NUEVO)
    current_kilometers = models.FloatField(default=0)
    last_date_support = models.DateField(null=True, blank=True)
    next_date_support = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'vehiculo'
        ordering = ['id']

# Modelo Conductor
class Conductor(models.Model):
    id = models.UUIDField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.RESTRICT, null=False, related_name='persona')
    licence_drive = models.CharField(max_length=30)
    date_entry = models.DateField()
    state = models.IntegerField(choices=estado_Conductor, default=estado_Conductor.NUEVO)

    class Meta:
        db_table = 'conductor'
        ordering = ['id']

# Modelo Asignacion
class Asignacion(models.Model):
    id = models.UUIDField(primary_key=True)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT, null=False, related_name='vehiculo')
    id_conductor = models.ForeignKey(Conductor, on_delete=models.RESTRICT, null=False, related_name='conductor')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    state = models.IntegerField(choices=estado_Asignacion, default=estado_Asignacion.NUEVO)

    class Meta:
        db_table = 'asignacion'
        ordering = ['id']

# Modelo TipoMantenimiento
class TipoMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'tipo_mantenimiento'
        rdering = ['id']

# Modelo Mantenimiento
class Mantenimiento(models.Model):
    id = models.UUIDField(primary_key=True)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT, null=False, related_name='vehiculo')
    description = models.CharField(max_length=250)
    date = models.DateField()
    kilometraje = models.FloatField()
    costo = models.FloatField()
    workshop = models.CharField(max_length=100)

    class Meta:
        db_table = 'mantenimiento'
        rdering = ['id']