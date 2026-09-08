from django.shortcuts import render, get_object_or_404, redirect
from .forms import NodoServidorForm
from infraestructura.models import NodoServidor
from django.shortcuts import get_object_or_404, redirect, render
from .forms import IncidenciaServidorForm
from .models import IncidenciaServidor, NodoServidor

def detalle_servidor(request, pk):
    servidor = get_object_or_404(NodoServidor, pk=pk)
    contexto = {'nodo': servidor}
    return render(request, 'infraestructura/detalle.html', contexto)

def editar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        form = NodoServidorForm(request.POST, instance=nodo)
        if form.is_valid():
            form.save()
            return redirect('detalle_servidor', pk=nodo.pk)
    else:
        form = NodoServidorForm(instance=nodo)
    return render(request, 'infraestructura/editar_servidor.html', {'form': form, 'nodo': nodo})

def eliminar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        nodo.delete()
        return redirect('home_servidores')
    return render(request, 'infraestructura/eliminar_servidor.html', {'nodo': nodo})

def lista_servidores(request):
	servidores = NodoServidor.objects.all()
	contexto = {'servidores': servidores}
	return render(request, 'infraestructura/index.html', contexto)

def crear_servidor(request):
    if request.method == 'POST':
        form = NodoServidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_servidores')
    else:
        form = NodoServidorForm()
    return render(request, 'infraestructura/crear_servidor.html', {'form': form})
from django.shortcuts import get_object_or_404, redirect, render
from .forms import IncidenciaServidorForm
from .models import IncidenciaServidor, NodoServidor


def detalle_servidor(request, pk):
  servidor = get_object_or_404(NodoServidor, pk=pk)
  incidencias = servidor.incidencias.all()
  form_incidencia = IncidenciaServidorForm()

  return render(
      request,
      'infraestructura/detalle.html',
      {
          'servidor': servidor,
          'incidencias': incidencias,
          'form_incidencia': form_incidencia,
      },
  )


def registrar_incidencia(request, servidor_id):
  servidor = get_object_or_404(NodoServidor, pk=servidor_id)

  if request.method == 'POST':
    form = IncidenciaServidorForm(request.POST)
    if form.is_valid():
      incidencia = form.save(commit=False)
      incidencia.servidor = servidor
      incidencia.save()

  return redirect('detalle_servidor', pk=servidor.id)


def marcar_resuelta(request, incidencia_id):
  incidencia = get_object_or_404(IncidenciaServidor, pk=incidencia_id)
  incidencia.resuelta = True
  incidencia.save()
  return redirect('detalle_servidor', pk=incidencia.servidor.id)




def detalle_servidor(request, pk):
  nodo = get_object_or_404(NodoServidor, pk=pk)
  incidencias = (
      nodo.incidencias.all()
  )  # usa el related_name='incidencias' del ForeignKey
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