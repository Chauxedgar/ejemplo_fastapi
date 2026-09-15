from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework import permissions, viewsets

from .forms import IncidenciaServidorForm, MantenimientoForm, NodoServidorForm
from .models import IncidenciaServidor, MantenimientoNodo, NodoServidor
from .serializers import (
    GroupSerializer,
    IncidenciaServidorSerializer,
    NodoServidorSerializer,
    UserSerializer,
)

# ==========================================
# 1. Vistas Basadas en Clases (Mantenimientos)
# ==========================================


class MantenimientoListView(ListView):
  model = MantenimientoNodo
  template_name = 'infraestructura/mantenimiento_list.html'
  context_object_name = 'mantenimientos'


class MantenimientoDetailView(DetailView):
  model = MantenimientoNodo
  template_name = 'infraestructura/mantenimiento_detail.html'
  context_object_name = 'mantenimiento'


class MantenimientoCreateView(CreateView):
  model = MantenimientoNodo
  form_class = MantenimientoForm
  template_name = 'infraestructura/mantenimiento_form.html'
  success_url = reverse_lazy('lista_mantenimientos')


class MantenimientoUpdateView(UpdateView):
  model = MantenimientoNodo
  form_class = MantenimientoForm
  template_name = 'infraestructura/mantenimiento_form.html'
  success_url = reverse_lazy('lista_mantenimientos')


class MantenimientoDeleteView(DeleteView):
  model = MantenimientoNodo
  template_name = 'infraestructura/mantenimiento_confirm_delete.html'
  success_url = reverse_lazy('lista_mantenimientos')


# ==========================================
# 2. Vistas Basadas en Funciones (Servidores e Incidencias)
# ==========================================


def lista_servidores(request):
  servidores = NodoServidor.objects.all()
  return render(
      request, 'infraestructura/index.html', {'servidores': servidores}
  )


def crear_servidor(request):
  if request.method == 'POST':
    form = NodoServidorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home_servidores')
  else:
    form = NodoServidorForm()
  return render(request, 'infraestructura/crear_servidor.html', {'form': form})


def detalle_servidor(request, pk):
  nodo = get_object_or_404(NodoServidor, pk=pk)
  incidencias = nodo.incidencias.all()
  form_incidencia = IncidenciaServidorForm()
  return render(
      request,
      'infraestructura/detalle.html',
      {
          'nodo': nodo,
          'incidencias': incidencias,
          'form_incidencia': form_incidencia,
      },
  )


def editar_servidor(request, pk):
  nodo = get_object_or_404(NodoServidor, pk=pk)
  if request.method == 'POST':
    form = NodoServidorForm(request.POST, instance=nodo)
    if form.is_valid():
      form.save()
      return redirect('detalle_servidor', pk=nodo.pk)
  else:
    form = NodoServidorForm(instance=nodo)
  return render(
      request,
      'infraestructura/editar_servidor.html',
      {'form': form, 'nodo': nodo},
  )


def eliminar_servidor(request, pk):
  nodo = get_object_or_404(NodoServidor, pk=pk)
  if request.method == 'POST':
    nodo.delete()
    return redirect('home_servidores')
  return render(
      request, 'infraestructura/eliminar_servidor.html', {'nodo': nodo}
  )


def registrar_incidencia(request, pk):
  nodo = get_object_or_404(NodoServidor, pk=pk)
  if request.method == 'POST':
    form = IncidenciaServidorForm(request.POST)
    if form.is_valid():
      incidencia = form.save(commit=False)
      incidencia.servidor = nodo
      incidencia.save()
  return redirect('detalle_servidor', pk=nodo.pk)


def marcar_resuelta(request, incidencia_id):
  incidencia = get_object_or_404(IncidenciaServidor, pk=incidencia_id)
  incidencia.resuelta = True
  incidencia.save()
  return redirect('detalle_servidor', pk=incidencia.servidor.pk)


# ==========================================
# 3. ViewSets para la API REST (JSON)
# ==========================================


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [permissions.IsAuthenticated]


class NodoServidorViewSet(viewsets.ModelViewSet):
  queryset = NodoServidor.objects.all()
  serializer_class = NodoServidorSerializer
  permission_classes = [permissions.AllowAny]


class IncidenciaServidorViewSet(viewsets.ModelViewSet):
  queryset = IncidenciaServidor.objects.all()
  serializer_class = IncidenciaServidorSerializer
  permission_classes = [permissions.AllowAny]