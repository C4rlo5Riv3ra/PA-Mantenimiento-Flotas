from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import profile_update, profile_view
from .views import *
from uuid import UUID

from .views import exportar_excel

router = DefaultRouter()


router.register(r'usuarios', UsuarioViewSet)
router.register(r'tipos-vehiculo', TipoVehiculoViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'conductores', ConductorViewSet)
router.register(r'asignaciones', AsignacionViewSet)
router.register(r'tipos-mantenimiento', TipoMantenimientoViewSet)
router.register(r'mantenimientos', MantenimientoViewSet)
router.register(r'alertas-mantenimiento', AlertaMantenimientoViewSet)
router.register(r'servicios-mantenimiento', ServicioMantenimientoViewSet)
router.register(r'detalles-mantenimiento', DetalleMantenimientoViewSet)

urlpatterns = [
    path('', index, name='index'), 

    path('api/', include(router.urls)),
    
    #VEHICULOS
    path('vehiculos/', listar_vehiculos, name='listar_vehiculos'),
    path('vehiculos/nuevo/', crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<uuid:id>/', editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<uuid:id>/', eliminar_vehiculo, name='eliminar_vehiculo'),


    #CONDUCTORES
    path('conductores/', listar_conductores, name='listar_conductores'),
    path('conductores/nuevo/', crear_conductor, name='crear_conductor'),
    path('conductores/editar/<uuid:id>/', editar_conductor, name='editar_conductor'),
    path('conductores/eliminar/<uuid:id>/', eliminar_conductor, name='eliminar_conductor'),

    #MANTENIMIENTO
    path('mantenimientos/', listar_mantenimientos, name='listar_mantenimientos'),
    path('mantenimientos/crear/', crear_mantenimiento, name='crear_mantenimiento'),
    path('mantenimientos/editar/<uuid:id>/', editar_mantenimiento, name='editar_mantenimiento'),
    path('mantenimientos/eliminar/<uuid:id>/', eliminar_mantenimiento, name='eliminar_mantenimiento'),
    path('ajax/filtrar-placas/', filtrar_placas, name='filtrar_placas'),

    #ALERTAS
    path('alertas/', listar_alertas, name='listar_alertas'),
    path('alertas/editar/<uuid:alerta_id>/', editar_alerta, name='editar_alerta'),
    path('alertas/eliminar/<uuid:alerta_id>/', eliminar_alerta, name='eliminar_alerta'),
    path('vehiculos/<uuid:vehiculo_id>/historial/', historial_mantenimiento, name='historial_mantenimiento'),

    #PERFIL
    path('perfil/', profile_view, name='profile'),
    path('perfil/actualizar/', profile_update, name='profile_update'),


    path('exportar-excel/', exportar_excel, name='exportar_excel'),
    path('exportar-conductores/', exportar_excel_con, name='exportar_excel_con'),
    path('exportar-mantenimientos/', exportar_excel_man, name='exportar_excel_man'),
    path('vehiculos/<uuid:vehiculo_id>/exportar_historial_excel/', exportar_excel_historial,
        name='exportar_excel_historial'
    ),
]
