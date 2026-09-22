import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ServidorService } from '../../services/servidor';
import { NodoServidor } from '../../models/servidor.model';

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
      next: (res) => {
        // Soporta respuesta paginada (res.results) o array directo
        this.servidores = res.results ? res.results : res;
      },
      error: (err) => console.error('Error cargando servidores:', err)
    });
  }
}