from django.db import models
from django.core.exceptions import ValidationError

def validate_ip(value):
    if value.startswith("192.168.100."):
        raise ValidationError("Las direcciones IP en el segmento 192.168.100.x están reservadas para pruebas internas de aislamiento")

    if value.startswith("10.10.10."):
        raise ValidationError("Las direcciones IP en el segmento 10.10.10.x están reservadas para pruebas internas de aislamiento")
from django.db import models
class IncidenciaServidor(models.Model):
  SEVERIDAD_CHOICES = [
      ('BAJA', 'Baja'),
      ('MEDIA', 'Media'),
      ('ALTA', 'Alta'),
      ('CRITICA', 'Crítica'),
  ]

  servidor = models.ForeignKey(
      'NodoServidor',
      on_delete=models.CASCADE,
      related_name='incidencias',
      verbose_name='Servidor',
  )
  titulo = models.CharField(max_length=150, verbose_name='Título')
  descripcion = models.TextField(verbose_name='Descripción')
  severidad = models.CharField(
      max_length=10,
      choices=SEVERIDAD_CHOICES,
      default='MEDIA',
      verbose_name='Severidad',
  )
  resuelta = models.BooleanField(
      default=False, verbose_name='Estado de resolución'
  )
  fecha_reporte = models.DateTimeField(
      auto_now_add=True, verbose_name='Fecha de reporte'
  )

def __str__(self):
    return f'[{self.severidad}] {self.titulo} - {self.servidor}'

class Meta: 
    ordering = ['-fecha_reporte']
    verbose_name = 'Incidencia de Servidor'
    verbose_name_plural = 'Incidencias de Servidores'

# Create your models here.
class NodoServidor(models.Model):
    # Opciones predefinidas para el panel
    MOTORES_CONTENEDOR = [
        ('docker', 'Docker'),
        ('podman', 'Podman'),
        ('lxc', 'LXC Linux Containers'),
        ('ninguno', 'Sin contenedores'),
    ]

    nombre_host = models.CharField(max_length=100, unique=True, verbose_name="Hostname")
    direccion_ip = models.GenericIPAddressField(verbose_name="Dirección IP", validators=[validate_ip])
    motor_contenedores = models.CharField(
        max_length=20,
        choices=MOTORES_CONTENEDOR,
        default='podman',
        verbose_name="Motor de contenedores"
    )

    proxy_inverso = models.BooleanField(default=True, verbose_name="¿Enrutado por NGINX?")
    en_produccion = models.BooleanField(default=True, verbose_name="Estado Producción")
    fecha_despliegue = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_host} [{self.direccion_ip}]"
            

class Meta:
    verbose_name = "Nodo de Servidor"
    verbose_name_plural = "Flota de Servidores"


class RegistroAuditoria(models.Model):
    servidor = models.ForeignKey(NodoServidor, on_delete=models.CASCADE, related_name='auditorias')
    detalles = models.TextField(verbose_name="Detalle del Evento")
    fecha_evento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.detalles} on {self.servidor.nombre_host} @ {self.fecha_evento}"

class Meta:
    verbose_name = "Registro de Auditoría"
    verbose_name_plural = "Registros de Auditoría"

class MantenimientoNodo(models.Model):
    TIPO_TAREA = [
        ('actualizacion', 'Actualización de sistema'),
        ('backup', 'Respaldo de Base de Datos'),
        ('seguridad','Parche de Seguridad'),
        ('hardware','Recisión de Hardware'),
    ]
    servidor = models.ForeignKey( 
        NodoServidor,  
        on_delete=models.CASCADE,
        related_name='mantenimientos',          
        verbose_name="Servidor Asignado"     
        )
    titulo_tarea = models.CharField(max_length=150, verbose_name="Título del Mantenimiento")     
    descripcion_tecnica = models.TextField(verbose_name="Descripción de la Tarea")     
    tipo = models.CharField(max_length=30, choices=TIPO_TAREA, default='actualizacion', 
verbose_name="Tipo de Tarea")     
    completado = models.BooleanField(default=False, verbose_name="¿Tarea Ejecutada?")     
    fecha_programada = models.DateTimeField(verbose_name="Fecha y Hora Programada")      
    def __str__(self):         
        return f"{self.titulo_tarea} - {self.servidor.nombre_host}"      
    class Meta:         
        verbose_name = "Mantenimiento de Servidor"         
        verbose_name_plural = "Programación de Mantenimientos" 