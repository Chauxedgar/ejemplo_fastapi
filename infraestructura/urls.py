from django.urls import include, path
from infraestructura import views
from rest_framework.routers import DefaultRouter

# Router para la API REST
router = DefaultRouter()
router.register(
    r'servidores', views.NodoServidorViewSet, basename='api-servidor'
)
router.register(
    r'incidencias', views.IncidenciaServidorViewSet, basename='api-incidencia'
)
router.register(r'users', views.UserViewSet, basename='api-user')
router.register(r'groups', views.GroupViewSet, basename='api-group')

urlpatterns = [
    # Rutas Web
    path('', views.lista_servidores, name='home_servidores'),
    path('servidor/nuevo/', views.crear_servidor, name='crear_servidor'),
    path(
        'servidor/<int:pk>/', views.detalle_servidor, name='detalle_servidor'
    ),
    path(
        'servidor/<int:pk>/editar/',
        views.editar_servidor,
        name='editar_servidor',
    ),
    path(
        'servidor/<int:pk>/eliminar/',
        views.eliminar_servidor,
        name='eliminar_servidor',
    ),
    path(
        'servidor/<int:pk>/incidencia/nueva/',
        views.registrar_incidencia,
        name='registrar_incidencia',
    ),
    path(
        'incidencia/<int:incidencia_id>/resolver/',
        views.marcar_resuelta,
        name='marcar_resuelta',
    ),
    # Rutas API REST
    path('api/', include(router.urls)),
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    ),
]