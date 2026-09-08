from django import forms
from .models import NodoServidor

class NodoServidorForm(forms.ModelForm):
    class Meta:
        model = NodoServidor
        fields = ['nombre_host', 'direccion_ip', 'motor_contenedores', 'proxy_inverso', 'en_produccion']
from django import forms
from .models import IncidenciaServidor


class IncidenciaServidorForm(forms.ModelForm):

  class Meta:
    model = IncidenciaServidor
    fields = ['titulo', 'descripcion', 'severidad']
    widgets = {
        'titulo': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Caída de servicio HTTP',
            }
        ),
        'descripcion': forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Detalles de la falla...',
            }
        ),
        'severidad': forms.Select(attrs={'class': 'form-select'}),
    }