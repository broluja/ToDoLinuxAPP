"""Creating Model for 'lists' table."""
import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from Model.database.settings import Base


class List(Base):
    """Model for data table 'lists'."""
    __tablename__ = 'lists'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)

    def to_dict(self):
        """
        Returns:
            dict
        """
        return {
            'id': self.id,
            'name': self.name
        }
