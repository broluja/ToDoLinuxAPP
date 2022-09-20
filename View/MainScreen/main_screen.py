from kivy.properties import ListProperty, StringProperty, NumericProperty, DictProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDColorPicker, MDDatePicker
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.boxlayout import MDBoxLayout

from Model.repository.task_repository import task_repository
from Model.repository.list_repository import list_repository
from Model.models.task_model import Task
from Controller.exceptions import DatabaseException


class Content(MDBoxLayout):
    """Dialog box for creating new Task."""
    task_id = ObjectProperty()
    counter = NumericProperty()
    priority = ObjectProperty()
    date = ObjectProperty()

    def get_date(self, instance, value, date_range):
        date = f'Due Date set to {value}'
        self.date = value
        self.parent.panel_cls.secondary_text = date

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.get_date)
        date_dialog.open()

    def set_priority(self, value):
        self.parent.panel_cls.tertiary_text = value
        self.priority = value.upper()


class MainScreenView(MDScreen):
    """Main screen for displaying tasks of chosen List."""
    tasks = ListProperty()
    selected_list = StringProperty()
    list = DictProperty()

    def __init__(self, **kwargs):
        super(MainScreenView, self).__init__(**kwargs)
        self.task_manager = task_repository
        self.list_manager = list_repository

    def init_list(self):
        try:
            my_list = self.list_manager.get_by_name(self.selected_list)
            self.list = {'ID': my_list.id, 'Name': self.selected_list}
        except Exception as e:
            print(e)

    def on_enter(self, *args):
        self.init_list()
        try:
            self.tasks = self.task_manager.get_tasks_by_list_id(self.list['ID'])
            self.populate_screen()
        except Exception as e:
            print(e)

    def populate_screen(self):
        for task in self.tasks:
            content = Content(task_id=task.id)
            content.ids.content.text = task.content
            panel = MDExpansionPanel(icon="linux-mint", content=content, panel_cls=MDExpansionPanelThreeLine(
                text=task.title,
                secondary_text=f'Due Date: {task.date.date()}',
                tertiary_text=f'{task.priority}',
                font_style='Body1',
                theme_text_color='Hint'
            ))
            self.ids.hidden.add_widget(panel)

    def on_leave(self):
        self.ids.hidden.clear_widgets(self.ids.hidden.children)
        self.tasks = []

    def add_task(self, text):
        task = MDExpansionPanel(icon="linux-mint", content=Content(), panel_cls=MDExpansionPanelThreeLine(
            text=text,
            secondary_text='',
            font_style='Body1',
            theme_text_color='Hint'
        ))
        self.ids.hidden.add_widget(task)
        self.ids.task.text = ''

    def save_task(self, task_id, title, content, date, priority):
        if task := self.task_manager.get_task_by_id(task_id):
            self.update_task(task, title, content, date, priority.upper(), False)
            return
        list_id = self.list['ID']
        self.task_manager.create({'list_id': list_id,
                                  'title': title,
                                  'content': content,
                                  'date': date,
                                  'priority': priority.upper(),
                                  'is_complete': False
                                  })

    def delete_task(self, task_id):
        try:
            task = self.task_manager.get_task_by_id(task_id)
            self.task_manager.remove(task.id)
        except Exception as e:
            print(e)
            return DatabaseException(message='Failed.')

    def update_task(self, task: Task, title, content, date, priority, is_complete):
        self.task_manager.update(task, fields={
            'title': title,
            'content': content,
            'date': date,
            'priority': priority,
            'is_complete': is_complete
        })

    def open_color_picker(self):
        color_picker = MDColorPicker(size_hint=(0.4, 0.8))
        color_picker.open()
        color_picker.bind(on_release=self.get_selected_color, )

    def get_selected_color(self, picker: MDColorPicker, type_color: str, selected_color):
        self.md_bg_color = selected_color
        picker.dismiss()
