from django.urls import path
from infraestructura.views import (
    crear_servidor,
    detalle_servidor,
    editar_servidor,
    eliminar_servidor,
    lista_servidores,
    marcar_resuelta,
    registrar_incidencia,
)

urlpatterns = [
    path('', lista_servidores, name='home_servidores'),
    path('servidor/nuevo/', crear_servidor, name='crear_servidor'),
    path('servidor/<int:pk>/', detalle_servidor, name='detalle_servidor'),
    path('servidor/<int:pk>/editar/', editar_servidor, name='editar_servidor'),
    path(
        'servidor/<int:pk>/eliminar/',
        eliminar_servidor,
        name='eliminar_servidor',
    ),
    path(
        'servidor/<int:pk>/incidencia/nueva/',
        registrar_incidencia,
        name='registrar_incidencia',
    ),
    path(
        'incidencia/<int:incidencia_id>/resolver/',
        marcar_resuelta,
        name='marcar_resuelta',
    ),
]