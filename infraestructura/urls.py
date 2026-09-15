from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
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
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'groups', views.GroupViewSet, basename='group')

urlpatterns = [
    # --- Servidores e Incidencias ---
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
    # --- Mantenimientos (Class-Based Views) ---
    path(
        'mantenimientos/',
        views.MantenimientoListView.as_view(),
        name='lista_mantenimientos',
    ),
    path(
        'mantenimientos/<int:pk>/',
        views.MantenimientoDetailView.as_view(),
        name='detalle_mantenimiento',
    ),
    path(
        'mantenimientos/nuevo/',
        views.MantenimientoCreateView.as_view(),
        name='crear_mantenimiento',
    ),
    path(
        'mantenimientos/<int:pk>/editar/',
        views.MantenimientoUpdateView.as_view(),
        name='editar_mantenimiento',
    ),
    path(
        'mantenimientos/<int:pk>/eliminar/',
        views.MantenimientoDeleteView.as_view(),
        name='eliminar_mantenimiento',
    ),
    # --- API REST y Autenticación ---
    path('api/', include(router.urls)),
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    ),
    # --- Swagger / OpenAPI Docs ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]