from typing import Optional
from datetime import datetime

from Model.models.list_model import List
from Model.models.task_model import Task
from Model.repository.base_repository import CRUDBase


class TaskRepository(CRUDBase[Task]):
    """ CRUD`s subclass for interaction with 'users' table """

    def get_by_title(self, title: str) -> Optional[List]:
        return self.db.query(Task).filter(Task.title == title).first()

    def get_tasks_by_list_id(self, list_id: str):
        return self.db.query(Task).filter(Task.list_id == list_id)

    def get_task_by_id(self, task_id):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_today_tasks(self):
        today = datetime.now().date()
        return self.db.query(Task).filter(Task.date == today)


task_repository = TaskRepository(Task)
