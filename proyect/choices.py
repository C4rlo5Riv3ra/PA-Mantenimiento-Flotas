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

class estado_Asignacion(models.IntegerChoices):
    ACTIVA = 1, 'Activa'
    FINALIZADA = 2, 'Finalizada'
    PENDIENTE = 3, 'Pendiente'
    CANCELADA = 4, 'Cancelada'

class estado_Alerta(models.IntegerChoices):
    ATENTIDA = 1, 'Atentida'
    PENDIENTE = 2, 'Pendiente'
    CANCELADA = 3, 'Cancelada'
    VENCIDA = 4, 'Vencida'