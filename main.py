import os
from pathlib import Path

from kivy.config import Config
Config.set("graphics", "width", "1800")
Config.set("graphics", "height", "1000")
from kivy.properties import ObjectProperty
from kivymd.app import MDApp

from View.Managers.manager_screen import ManagerScreen

os.environ['LINUX_TODO_APP'] = str(Path(__file__).parent)


class LinuxTodoApp(MDApp):
    """Linux App for scheduling tasks."""
    data = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Gray'
        self.manager_screen = ManagerScreen()

    def __str__(self):
        return 'Linux ToDo App'

    def build(self):
        self.manager_screen.add_widget(self.manager_screen.create_screen('list'))
        return self.manager_screen


LinuxTodoApp().run()
