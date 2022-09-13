import uuid
import enum

from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID

from Model.database.settings import Base


class TypeEnum(enum.Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

    def __str__(self):
        return self.value.title()


class Task(Base):
    """ Model for data table 'tasks' """

    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    list_id = Column(ForeignKey('lists.id'), unique=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime)
    priority = Column(Enum(TypeEnum))
    is_complete = Column(Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'list_id': self.list_id,
            'title': self.title,
            'content': self.content,
            'date': self.date,
            'priority': self.priority,
            'is_complete': self.is_complete
        }
