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

  getServidores(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/servidores/`);
  }

  getServidor(id: number): Observable<NodoServidor> {
    return this.http.get<NodoServidor>(`${this.apiUrl}/servidores/${id}/`);
  }
  getIncidencias(): Observable<Incidencia[]> {
    return this.http.get<Incidencia[]>(`${this.apiUrl}/incidencias/`);
  }
  
  getIncidencia(id: number): Observable<Incidencia> {
    return this.http.get<Incidencia>(`${this.apiUrl}/incidencias/${id}/`);
  }

  // --- MÉTODOS CRUD COMPLETOS ---
  crearServidor(servidor: Partial<NodoServidor>): Observable<NodoServidor> {
    return this.http.post<NodoServidor>(`${this.apiUrl}/servidores/`, servidor);
  }

  actualizarServidor(id: number, servidor: Partial<NodoServidor>): Observable<NodoServidor> {
    return this.http.put<NodoServidor>(`${this.apiUrl}/servidores/${id}/`, servidor);
  }

  eliminarServidor(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/servidores/${id}/`);
  }

  crearIncidencia(incidencia: Incidencia): Observable<Incidencia> {
    return this.http.post<Incidencia>(`${this.apiUrl}/incidencias/`, incidencia);
  }

  resolverIncidencia(id: number): Observable<Incidencia> {
    return this.http.patch<Incidencia>(`${this.apiUrl}/incidencias/${id}/`, { resuelta: true });
  }
}