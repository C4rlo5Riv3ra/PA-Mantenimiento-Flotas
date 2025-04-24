from django.db import models
from proyect.choices import estado_Usuario
import uuid
# Create your models here.
# MODELOS
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    doc_identity = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=80)

    class Meta:
        db_table = "persona"

class Rol(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "rol"

class EstadoUsuario(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "estado_usuario"

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoUsuario, on_delete=models.CASCADE)

    class Meta:
        db_table = "usuario"
