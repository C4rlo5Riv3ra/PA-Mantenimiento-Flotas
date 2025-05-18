from django import forms
from .models import (
    Persona, Usuario, Vehiculo, Conductor, Asignacion,
    Mantenimiento, AlertaMantenimiento, ServicioMantenimiento, DetalleMantenimiento
)








#DJANGO REST FRAMEWORK
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__'

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class AlertaMantenimientoForm(forms.ModelForm):
    class Meta:
        model = AlertaMantenimiento
        fields = '__all__'

class ServicioMantenimientoForm(forms.ModelForm):
    class Meta:
        model = ServicioMantenimiento
        fields = '__all__'

class DetalleMantenimientoForm(forms.ModelForm):
    class Meta:
        model = DetalleMantenimiento
        fields = '__all__'
