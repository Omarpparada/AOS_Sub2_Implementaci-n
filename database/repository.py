from datetime import datetime
from typing import List, Tuple
from sqlalchemy import and_, or_, func
from database.models import ModeloVehiculo

from database.session import SessionLocal

class Repository:
    def __init__(self) -> None:
        self.db = SessionLocal()

    def __del__(self) -> None:
        self.db.close()

    def get_vehiculos(self)-> List:
        print(self.db.query(ModeloVehiculo).all())

    def create_user(self, user_in: User):
        user_created = UserEntity(**dict(user_in))
        self.db.add(user_created)
        self.db.commit()
        self.db.refresh(user_created)
        return user_created

    