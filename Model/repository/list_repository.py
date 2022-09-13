from typing import Optional

from Model.models.list_model import List
from Model.repository.base_repository import CRUDBase


class ListRepository(CRUDBase[List]):
    """ CRUD`s subclass for interaction with 'users' table """

    def get_by_name(self, name: str) -> Optional[List]:
        return self.db.query(List).filter(List.name == name).first()

    def get_by_id(self, list_id: str):
        return self.db.query(List).filter(List.id == list_id)


list_repository = ListRepository(List)
