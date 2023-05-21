from datetime import date
from pydantic import AnyUrl, BaseModel, Field, constr

class vehiculos(BaseModel):
    id_vehiculo: str
    marca: str
    modelo: str
    fecha: date
    estado: str
    dni: str

    class Config:
        orm_mode = True