from django.db import models
from django.core.exceptions import ValidationError

def validate_ip(value):
    if value.startswith("192.168.100."):
        raise ValidationError("Las direcciones IP en el segmento 192.168.100.x están reservadas para pruebas internas de aislamiento")

    if value.startswith("10.10.10."):
        raise ValidationError("Las direcciones IP en el segmento 10.10.10.x están reservadas para pruebas internas de aislamiento")


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
