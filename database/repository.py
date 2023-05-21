from datetime import datetime
from typing import List, Tuple
from sqlalchemy import and_, or_, func
from database.models import VehiculosEntity

from database.session import SessionLocal

class Repository:
    def __init__(self) -> None:
        self.db = SessionLocal()

    def __del__(self) -> None:
        self.db.close()

    def get_vehiculos(self)-> List:
        prueba = self.db.query(VehiculosEntity).first()
        print(prueba.modelo)
        return prueba

    
    