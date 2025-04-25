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