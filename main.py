from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos
class Estudiante(BaseModel):
    id: int
    nombre: str
    programa: str
    promedio: float

# Datos simulados (tabla en memoria)
tabla_estudiantes: List[Estudiante] = [
    Estudiante(id=1, nombre="Ana Pérez", programa="Ingeniería Acuícola", promedio=4.2),
    Estudiante(id=2, nombre="Luis Gómez", programa="Ingeniería de Sistemas", promedio=3.8),
    Estudiante(id=3, nombre="María Torres", programa="Producción Acuícola", promedio=4.5),
]

# --- ENDPOINTS REST ---

# Raíz
@app.get("/")
def raiz():
    return {"mensaje": "Bienvenido a la API de estudiantes"}

# READ: obtener todos
@app.get("/estudiantes", response_model=List[Estudiante])
def obtener_estudiantes():
    return tabla_estudiantes

# READ: obtener uno por id
@app.get("/estudiantes/{estudiante_id}", response_model=Estudiante)
def obtener_estudiante(estudiante_id: int):
    for estudiante in tabla_estudiantes:
        if estudiante.id == estudiante_id:
            return estudiante
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

# CREATE: agregar nuevo
@app.post("/estudiantes", response_model=Estudiante)
def crear_estudiante(estudiante: Estudiante):
    # Validar que no exista el mismo id
    for e in tabla_estudiantes:
        if e.id == estudiante.id:
            raise HTTPException(status_code=400, detail="ID ya existe")
    tabla_estudiantes.append(estudiante)
    return estudiante

# UPDATE: modificar existente
@app.put("/estudiantes/{estudiante_id}", response_model=Estudiante)
def actualizar_estudiante(estudiante_id: int, datos: Estudiante):
    for i, estudiante in enumerate(tabla_estudiantes):
        if estudiante.id == estudiante_id:
            tabla_estudiantes[i] = datos
            return datos
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

# DELETE: eliminar existente
@app.delete("/estudiantes/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int):
    for estudiante in tabla_estudiantes:
        if estudiante.id == estudiante_id:
            tabla_estudiantes.remove(estudiante)
            return {"mensaje": f"Estudiante con id {estudiante_id} eliminado"}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")