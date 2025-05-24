import uuid
from django.db import models
from django.utils import timezone
from accounts.managers import UsuarioManager
from proyect.choices import *


from django.contrib.auth.models import AbstractBaseUser 
from django.contrib.auth.models import Group, PermissionsMixin

from accounts.managers import UsuarioManager
from proyect.choices import estado_Usuario, rol


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=60)
    id_rol = models.IntegerField(choices=rol, default=3)
    state = models.IntegerField(choices=estado_Usuario, default=1)
    last_date_support = models.DateField(null=True, blank=True)
    next_date_support = models.DateField(null=True, blank=True)
    
    # Campos obligatorios para Django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        db_table = "usuario"
        ordering = ['id']

    def __str__(self):
        return self.email

# Modelo Tipo Vehiculo
class TipoVehiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'tipo_vehiculo'
        ordering = ['id']

    def __str__(self):
        return self.name

# Modelo Vehiculo
class Vehiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    placa = models.CharField(max_length=15, unique=True)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField()
    id_tipo_vehiculo = models.ForeignKey(
        TipoVehiculo, on_delete=models.RESTRICT, null=False, related_name='vehiculos')
    state = models.IntegerField(
        choices=estado_Vehiculo, default=estado_Vehiculo.NUEVO)
    current_kilometers = models.FloatField(default=0)
    last_date_support = models.DateField(null=True, blank=True)
    next_date_support = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'vehiculo'
        ordering = ['id']

    def __str__(self):
        return self.placa

#Modelo conductor
class Conductor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    doc_identity = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    licence_drive = models.CharField(max_length=30)
    date_entry = models.DateField(default=timezone.now)
    state = models.IntegerField(choices=estado_Conductor, default=1)

    class Meta:
        db_table = 'conductor'
        ordering = ['id']

    def __str__(self):
        return f"{self.name} {self.lastname}"
 

# Modelo de Asignacion
class Asignacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.RESTRICT, null=False, related_name='asignaciones')
    id_conductor = models.ForeignKey(
        Conductor, on_delete=models.RESTRICT, null=False, related_name='asignaciones')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    state = models.IntegerField(
        choices=estado_Asignacion, default=estado_Asignacion.ACTIVA)

    class Meta:
        db_table = 'asignacion'
        ordering = ['id']

# Modelo TipoMantenimiento
class TipoMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'tipo_mantenimiento'
        ordering = ['id']

# Modelo Mantenimiento
class Mantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.RESTRICT, null=False, related_name='mantenimientos')
    description = models.CharField(max_length=250)
    date = models.DateField()
    kilometraje = models.FloatField()
    costo = models.FloatField()
    workshop = models.CharField(max_length=100)
    tipo = models.IntegerField(choices=TMantenimiento, default=TMantenimiento.PREVENTIVO)
    
    fecha_programada = models.DateField(null=True, blank=True)
    km_programado = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'mantenimiento'
        ordering = ['id']

    def __str__(self):
        return f"{self.tipo()} - {self.id_vehiculo.placa} - {self.description}"
    
# Modelo AlertaMantenimiento
class AlertaMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.RESTRICT, null=False, related_name='alertas_mantenimiento')
    mensaje = models.CharField(max_length=250)
    fecha_alerta = models.DateField()

    class Meta:
        db_table = 'alerta_mantenimiento'
        ordering = ['id']
    def __str__(self):
        return f"Alerta para {self.vehiculo.placa} - {self.mensaje}"


# Modelo ServicioMantenimiento
class ServicioMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.RESTRICT, null=False, related_name='servicios_mantenimiento')
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'servicio_mantenimiento'
        ordering = ['id']


# Modelo DetalleMantenimiento
class DetalleMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.RESTRICT, null=False, related_name='detalles_mantenimiento')
    mantenimiento = models.ForeignKey(
        Mantenimiento, on_delete=models.CASCADE, related_name='detalles')
    servicio = models.ForeignKey(
        ServicioMantenimiento, on_delete=models.CASCADE, related_name='detalles')

    class Meta:
        db_table = 'detalle_mantenimiento'
        ordering = ['id']


