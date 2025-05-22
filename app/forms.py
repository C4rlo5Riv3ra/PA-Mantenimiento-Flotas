from django import forms
from .models import (
    Usuario, Vehiculo, Conductor, Asignacion,
    Mantenimiento, AlertaMantenimiento, ServicioMantenimiento, DetalleMantenimiento
)

class AlertaForm(forms.ModelForm):
    class Meta:
        model = AlertaMantenimiento
        fields = ['mensaje', 'fecha_alerta']
        widgets = {
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'fecha_alerta': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }



#DJANGO REST FRAMEWORK
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_kilometers': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_tipo_vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'last_date_support': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_date_support': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        
class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'doc_identity': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'licence_drive': forms.TextInput(attrs={'class': 'form-control'}),
            'date_entry': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
        }

        
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'id_vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'workshop': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_programada': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'km_programado': forms.NumberInput(attrs={'class': 'form-control'}),
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
