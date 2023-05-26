from datetime import date, datetime
from typing import List, Tuple
from sqlalchemy import and_, or_, func
from database.models import Ordering1, VehiculosEntity

from database.session import SessionLocal

class Repository:
    def __init__(self) -> None:
        self.db = SessionLocal()

    def __del__(self) -> None:
        self.db.close()

    def get_vehiculos(self, ordering, order)-> List:
        if order !=None:
            if ordering==Ordering1.ASC:
                return self.db.query(VehiculosEntity).order_by(VehiculosEntity.id_vehiculo.asc()).all()
            else:
                return self.db.query(VehiculosEntity).order_by(VehiculosEntity.id_vehiculo.desc()).all()
        else:
            return self.db.query(VehiculosEntity).all()
        
    def post_vehiculos(self, body):
        vehiculo= self.db.add(VehiculosEntity(id_vehiculo=body.id.__root__ ,
            marca = body.marca.__root__ ,
            modelo =  body.modelo.__root__ ,
            fecha = body.fecha.__root__ ,
            estado = body.Estado.name,
            dni =body.DNI.__root__ ))
        self.db.commit()
        return self.get_vehiculos_by_vin(body.id.__root__)
    
    def get_vehiculos_by_dni(self, dni):
        return self.db.query(VehiculosEntity).where(VehiculosEntity.dni== dni).all()
    
    def get_vehiculos_by_dni_and_estado(self, dni, estado):
        return self.db.query(VehiculosEntity).where(VehiculosEntity.dni== dni, VehiculosEntity.estado==estado.name).all()
    
    def get_vehiculos_by_estados(self, estado):
        return self.db.query(VehiculosEntity).where(VehiculosEntity.estado==estado.name).all()

    def get_vehiculos_by_vin(self, vin):
        return self.db.query(VehiculosEntity).where(VehiculosEntity.id_vehiculo==vin).first()
    
    def delete(self, vin):
        vehiculo=self.get_vehiculos_by_vin(vin)
        if vehiculo:
            self.db.delete(vehiculo)
            self.db.commit()

    def put(self, body, vin):
        vehiculo=self.get_vehiculos_by_vin(vin)
        if vehiculo:
            self.db.delete(vehiculo)
            if body.modelo:
                vehiculo.modelo=body.modelo.__root__ 
            if body.fecha:
                vehiculo.fecha= body.fecha.__root__ 
            if body.Estado:
                vehiculo.estado = body.Estado.name,
            self.db.add(vehiculo)
            self.db.commit()