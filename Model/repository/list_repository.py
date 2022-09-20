"""ORM model for 'list'."""
import typing

from Model.models.list_model import List
from Model.repository.base_repository import CRUDBase


class ListRepository(CRUDBase[List]):
    """ CRUD`s subclass for interaction with 'lists' table """

    def get_by_name(self, name: str) -> typing.Optional[List]:
        """
        Args:
            name (str): string value, name of the list.

        Returns:
            list object.
        """
        return self.db.query(List).filter(List.name == name).first()

    def get_by_id(self, list_id: str) -> typing.Optional[List]:
        """
        Args:
            list_id (str): id of the list

        Returns:
            list object.
        """
        return self.db.query(List).filter(List.id == list_id).first()


list_repository = ListRepository(List)
