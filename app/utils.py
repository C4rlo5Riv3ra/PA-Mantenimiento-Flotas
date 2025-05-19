# app/utils.py
from datetime import date, timedelta
from .models import Vehiculo, Mantenimiento, AlertaMantenimiento

def generar_alertas():
    hoy = date.today()
    proximos_dias = hoy + timedelta(days=7)

    mantenimientos = Mantenimiento.objects.filter(
        fecha_programada__isnull=False,
        fecha_programada__lte=proximos_dias
    )

    for m in mantenimientos:
        mensaje_fecha = f"Mantenimiento programado para el {m.fecha_programada} en vehículo {m.id_vehiculo.placa}"
        AlertaMantenimiento.objects.get_or_create(
            id_vehiculo=m.id_vehiculo,
            mensaje=mensaje_fecha,
            fecha_alerta=hoy
        )

    mantenimientos_km = Mantenimiento.objects.filter(
        km_programado__isnull=False
    )

    for m in mantenimientos_km:
        if m.id_vehiculo.current_kilometers >= m.km_programado:
            mensaje_km = f"Vehículo {m.id_vehiculo.placa} ha superado el kilometraje programado ({m.km_programado} km)"
            AlertaMantenimiento.objects.get_or_create(
                id_vehiculo=m.id_vehiculo,
                mensaje=mensaje_km,
                fecha_alerta=hoy
            )
