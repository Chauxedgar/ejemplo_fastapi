import { Routes } from '@angular/router';
import { ListaServidoresComponent } from './components/lista-servidores/lista-servidores.component';
import { DetalleServidorComponent } from './components/detalle-servidor/detalle-servidor.component';

export const routes: Routes = [
  { path: '', component: ListaServidoresComponent },
  { path: 'servidor/:id', component: DetalleServidorComponent },
  { path: '**', redirectTo: '' }
];