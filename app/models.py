from django.db import models
from proyect.choices import estado_Usuario

# Create your models here.
class Usuario(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=60, null=False)
    password = models.CharField(max_length=60, null=False)
    id_rol = models.CharField(max_length=60, null=False)
    estado = models.IntegerField(choices=estado_Usuario, default=estado_Usuario.ACTIVO)

    class Meta:
        db_table = "usuario"
        ordering = ['id']


