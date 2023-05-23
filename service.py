from typing import List

from database.repository import Repository


class VehiculosService:

    def __init__(self) -> None:
        self.repository = Repository()
    
    def get_vehiculos(self, ordering, order):
        return self.repository.get_vehiculos(ordering, order)
    
    def post_vehiculos(self, body):
        return self.repository.post_vehiculos(body)
    
    def get_vehiculos_by_dni(self, dni):
        return self.repository.get_vehiculos_by_dni(dni)
    
    def get_vehiculos_by_dni_and_estado(self, dni, estado):
        return self.repository.get_vehiculos_by_dni_and_estado(dni, estado)
    
    def get_vehiculos_by_estados(self, estado):
        return self.repository.get_vehiculos_by_estados(estado)
    
    def get_vehiculos_by_vin(self, vin):
        return self.repository.get_vehiculos_by_vin(vin)
    
    def delete(self, vin):
        self.repository.delete(vin)
    
    def put(self, body, vin):
        self.repository.put(body, vin)
