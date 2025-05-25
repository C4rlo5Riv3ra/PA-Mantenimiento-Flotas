from django.db import models

class estado_Usuario(models.IntegerChoices):
    ACTIVO = 1, 'Activo'
    INACTIVO = 2, 'Inactivo'
    PENDIENTE = 3 ,'Pendiente'
    SUSPENDIDO = 4, 'Suspendido'

class estado_Conductor(models.IntegerChoices):
    DISPONIBLE = 1, 'Disponible'
    NO_DISPONIBLE = 2, 'No Disponible'
    DE_BAJA = 3, 'De baja'
    SUSPENDIDO = 4, 'Suspendido'

# clase vehiculo aun no esta implementada en la base de datos
class estado_Vehiculo(models.IntegerChoices):
    NUEVO = 1, 'Nuevo'
    DETERIORADO = 2, 'Deteriorado'
    USADO = 3, 'Usado'
    REPARADO = 4, 'Reparado'

class estado_Asignacion(models.IntegerChoices):
    ACTIVA = 1, 'Activa'
    FINALIZADA = 2, 'Finalizada'
    PENDIENTE = 3, 'Pendiente'
    CANCELADA = 4, 'Cancelada'


class TMantenimiento(models.IntegerChoices):
    PREVENTIVO = 1, 'Preventivo'
    CORRECTIVO = 2, 'Correctivo'

class estado_Alerta(models.IntegerChoices):
    ATENTIDA = 1, 'Atentida'
    PENDIENTE = 2, 'Pendiente'
    CANCELADA = 3, 'Cancelada'
    VENCIDA = 4, 'Vencida'

class rol(models.IntegerChoices):
    CONDUCTOR = 1, 'Conductor'
    TECNICO = 2, 'Tecnico'
    ADMIN = 3, 'Admin'