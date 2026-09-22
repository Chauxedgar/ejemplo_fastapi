import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ServidorService } from '../../services/servidor';
import { NodoServidor, Incidencia } from '../../models/servidor.model';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-detalle-servidor',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './detalle-servidor.component.html'
})
export class DetalleServidorComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private servidorService = inject(ServidorService);

  servidor?: NodoServidor;
  nuevaIncidencia: Partial<Incidencia> = {
    severidad: 'MEDIA'
  };

  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');
    const id = idParam ? Number(idParam) : 0;
    if (id) {
      this.cargarDetalle(id);
    }
  }

  cargarDetalle(id: number): void {
    this.servidorService.getServidor(id).subscribe({
      next: (res: NodoServidor) => {
        this.servidor = res;
      },
      error: (err: HttpErrorResponse) => {
        console.error('Error al cargar servidor:', err);
      }
    });
  }

  guardarIncidencia(): void {
    if (!this.servidor || !this.nuevaIncidencia.titulo || !this.nuevaIncidencia.descripcion) return;

    const payload: Incidencia = {
      servidor: this.servidor.id,
      titulo: this.nuevaIncidencia.titulo,
      descripcion: this.nuevaIncidencia.descripcion,
      severidad: this.nuevaIncidencia.severidad || 'MEDIA',
      resuelta: false
    };

    this.servidorService.crearIncidencia(payload).subscribe({
      next: () => {
        this.nuevaIncidencia = { severidad: 'MEDIA' };
        if (this.servidor) {
          this.cargarDetalle(this.servidor.id);
        }
      },
      error: (err: HttpErrorResponse) => {
        console.error('Error registrando incidencia:', err);
      }
    });
  }

  resolver(incidenciaId: number): void {
    this.servidorService.resolverIncidencia(incidenciaId).subscribe({
      next: () => {
        if (this.servidor) {
          this.cargarDetalle(this.servidor.id);
        }
      },
      error: (err: HttpErrorResponse) => {
        console.error('Error al resolver incidencia:', err);
      }
    });
  }
}