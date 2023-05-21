import grpc
import math

from typing import List

from database.repository import Repository


class UserService:

    def __init__(self) -> None:
        self.repository = Repository()

    def get_user_by_id(self, user_id: str):
        return self.repository.get_user_by_id(user_id)
    def get_vehiculos(self):
        return self.repository.get_vehiculos()