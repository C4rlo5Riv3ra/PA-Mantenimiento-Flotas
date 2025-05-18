import uuid
from django.db import models
from proyect.choices import *

# Modelo Persona


class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    doc_identity = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=80)

    class Meta:
        db_table = "persona"
        ordering = ['id']

    def __str__(self):
        return self.name

# Modelo Usuario


class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=60, null=False)
    password = models.CharField(max_length=60, null=False)
    id_rol = models.IntegerField(choices=rol)
    id_person = models.ForeignKey(
        Persona, on_delete=models.RESTRICT, null=False, related_name='usuarios')
    state = models.IntegerField(
        choices=estado_Usuario, default=estado_Usuario.ACTIVO)
    last_date_support = models.DateField(null=True, blank=True)
    next_date_support = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "usuario"
        ordering = ['id']

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

# Modelo Conductor


class Conductor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_persona = models.ForeignKey(
        Persona, on_delete=models.RESTRICT, null=False, related_name='conductores')
    licence_drive = models.CharField(max_length=30)
    date_entry = models.DateField()
    state = models.IntegerField(
        choices=estado_Conductor, default=estado_Conductor.DISPONIBLE)

    class Meta:
        db_table = 'conductor'
        ordering = ['id']
    def __str__(self):
            return f"{self.id_persona.name} {self.id_persona.lastname}"
    

# Modelo Asignacion


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
