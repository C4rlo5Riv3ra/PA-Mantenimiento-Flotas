import uuid
from django.db import models 


class Perfil(models.Model):
    perfil_id = models.IntegerField(primary_key=True)
    perfil_nombre = models.CharField(max_length=100, null=False)

    def __str__(self):
        return '%d: %s' % (self.perfil_id, self.perfil_nombre)

    class Meta:
        db_table = 'perfiles'

