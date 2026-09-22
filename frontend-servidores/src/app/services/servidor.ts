import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { NodoServidor, Incidencia } from '../models/servidor.model';

@Injectable({
  providedIn: 'root'
})
export class ServidorService {
  private http = inject(HttpClient);
  private apiUrl = 'http://127.0.0.1:8000/api';

  // Servidores
  getServidores(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/servidores/`);
  }

  getServidor(id: number): Observable<NodoServidor> {
    return this.http.get<NodoServidor>(`${this.apiUrl}/servidores/${id}/`);
  }

  // Incidencias
  crearIncidencia(incidencia: Incidencia): Observable<Incidencia> {
    return this.http.post<Incidencia>(`${this.apiUrl}/incidencias/`, incidencia);
  }

  resolverIncidencia(id: number): Observable<Incidencia> {
    return this.http.patch<Incidencia>(`${this.apiUrl}/incidencias/${id}/`, { resuelta: true });
  }
}