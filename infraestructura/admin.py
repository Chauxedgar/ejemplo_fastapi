from django.contrib import admin
from infraestructura.models import NodoServidor, RegistroAuditoria

# Django actions
@admin.action(description="Activar producción masiva")
def marcar_como_produccion(modeladmin, request, queryset):
    updated = queryset.update(en_produccion=True)

    print(f"{updated} dato(s) actualizado(s), en producción.")

@admin.action(description="Poner en mantenimiento")
def marcar_como_mantenimiento(modeladmin, request, queryset):
    updated = queryset.update(en_produccion=False)

    print(f"{updated} dato(s) actualizado(s), en mantenimiento.")

# Register your models here.
@admin.register(NodoServidor)
class NodoServidorAdmin(admin.ModelAdmin):
    # Registrar acciones en la tabla
    actions = [marcar_como_produccion, marcar_como_mantenimiento,]

    # Columnas que se mostrarán en la tabla principal
    list_display = ('nombre_host', 'direccion_ip', 'motor_contenedores', 'proxy_inverso', "en_produccion")

    # Filtros laterales para hacer búsquedas rápidas
    list_filter = ('motor_contenedores', 'proxy_inverso', "en_produccion")

    # Barra de búsqueda superior
    search_fields = ('nombre_host', 'direccion_ip')

    # Orden por defecto
    ordering = ('-fecha_despliegue',)

@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la tabla principal
    list_display = ('servidor', 'detalles')
