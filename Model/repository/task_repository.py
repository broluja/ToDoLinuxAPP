"""ORM model for 'task'."""
from typing import Optional, List
from datetime import datetime

from Model.models.task_model import Task
from Model.repository.base_repository import CRUDBase


class TaskRepository(CRUDBase[Task]):
    """ CRUD`s subclass for interaction with 'tasks' table """

    def get_by_title(self, title: str) -> Optional[Task]:
        """
        Args:
            title (str): string value, title of the task.

        Returns:
            list object.
        """
        return self.db.query(Task).filter(Task.title == title).first()

    def get_tasks_by_list_id(self, list_id: str) -> Optional[List[Task]]:
        """
        Args:
            list_id (str): string value, id of the list from which we are fetching tasks.

        Returns:
            list of task objects.
        """
        return self.db.query(Task).filter(Task.list_id == list_id).first()

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Args:
            task_id (str): string value, id of the task.

        Returns:
            task object.
        """
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_today_tasks(self) -> Optional[List[Task]]:
        """
        Returns:
            list of tasks that are scheduled for today`s date.
        """
        today = datetime.now().date()
        return self.db.query(Task).filter(Task.date == today).all()


task_repository = TaskRepository(Task)
