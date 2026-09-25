import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ServidorService } from '../../services/servidor';
import { NodoServidor } from '../../models/servidor.model';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-lista-servidores',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './lista-servidores.component.html'
})
export class ListaServidoresComponent implements OnInit {
  private servidorService = inject(ServidorService);
  servidores: NodoServidor[] = [];

  ngOnInit(): void {
    this.cargarServidores();
  }

  cargarServidores(): void {
    this.servidorService.getServidores().subscribe({
      next: (res: any) => {
        this.servidores = Array.isArray(res) ? res : res.results;
      },
      error: (err: HttpErrorResponse) => {
        console.error('Error cargando servidores:', err);
      }
    });
  }

  // --- ACCIÓN DE ELIMINAR ---
  eliminar(id: number): void {
    if (confirm('¿Estás seguro de eliminar este servidor de la infraestructura?')) {
      this.servidorService.eliminarServidor(id).subscribe({
        next: () => {
          // Recarga la lista actualizando el arreglo local
          this.servidores = this.servidores.filter(s => s.id !== id);
        },
        error: (err: HttpErrorResponse) => {
          console.error('Error al eliminar servidor:', err);
        }
      });
    }
  }

  // --- ACCIÓN DE NUEVO SERVIDOR (Prueba rápida con datos por defecto o formulario) ---
  abrirModalCrear(): void {
    const nombre = prompt('Ingrese el nombre de host (ej: nodo-web-02):');
    const ip = prompt('Ingrese la dirección IP (ej: 192.168.1.50):');
    
    if (nombre && ip) {
      const nuevo: Partial<NodoServidor> = {
        nombre_host: nombre,
        direccion_ip: ip,
        motor_contenedores: 'DOCKER',
        proxy_inverso: true,
        en_produccion: true,
        fecha_despliegue: new Date().toISOString().split('T')[0]
      };

      this.servidorService.crearServidor(nuevo).subscribe({
        next: () => {
          this.cargarServidores(); // Refresca la lista
        },
        error: (err) => console.error('Error creando servidor:', err)
      });
    }
  }
  
  
}