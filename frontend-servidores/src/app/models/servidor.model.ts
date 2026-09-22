export interface Incidencia {
  id?: number;
  servidor: number;
  servidor_nombre?: string;
  titulo: string;
  descripcion: string;
  severidad: 'BAJA' | 'MEDIA' | 'ALTA' | 'CRITICA';
  resuelta: boolean;
  fecha_reporte?: string;
}

export interface NodoServidor {
  id: number;
  nombre_host: string;
  direccion_ip: string;
  motor_contenedores: string;
  motor_contenedores_display?: string;
  proxy_inverso: boolean;
  en_produccion: boolean;
  fecha_despliegue: string;
  incidencias?: Incidencia[];
}