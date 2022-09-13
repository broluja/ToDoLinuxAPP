from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout

from Model.repository.list_repository import list_repository
from Model.repository.task_repository import task_repository
from View.Managers.notification_manager import NotificationManager
from Controller.exceptions import DatabaseException


class DialogContent(MDBoxLayout):

    def __init__(self, **kwargs):
        super(DialogContent, self).__init__(**kwargs)
        self.notifier = NotificationManager()
        self.list_manager = list_repository

    def create_list(self):
        list_name = self.ids.list_field.text
        if not list_name:
            self.notifier.notify('Please enter a name for the list.')
            return
        try:
            list_repository.create({'name': list_name})
        except Exception as e:
            raise DatabaseException(message=str(e)) from e


class ListScreenView(MDScreen):
    lists = ListProperty()
    selected = StringProperty()
    dialog_box = ObjectProperty()
    scheduled_tasks = ListProperty([])
    today_tasks = ListProperty([])

    def __init__(self, **kwargs):
        super(ListScreenView, self).__init__(**kwargs)
        self.list_manager = list_repository
        self.task_manager = task_repository
        self.get_lists()

    def on_enter(self, *args):
        self.populate_lists()

    def get_lists(self):
        lists = list_repository.get_multi()
        for created_list in lists:
            self.lists.append({'Name': created_list.name, 'Populated': False})

    def populate_lists(self):
        for table in self.lists:
            if not table['Populated']:
                widget = OneLineListItem(text=table['Name'], font_style='H6', theme_text_color='Hint',
                                         on_release=lambda x: self.select_list(x.text))
                widget.id = table['Name']
                table['Populated'] = True
                self.ids.listing.add_widget(widget)

    def select_list(self, selected_list):
        self.selected = selected_list
        self.manager.switch_screen('main', selected_list=self.selected)

    def open_dialog(self):
        dialog = MDDialog(
            pos_hint={'center_x': .2, 'top': .9},
            title='Create new List',
            type='custom',
            content_cls=DialogContent()
        )
        self.dialog_box = dialog
        self.dialog_box.open()

    def refresh_lists(self):
        self.ids.listing.clear_widgets(self.ids.listing.children)
        self.get_lists()
        self.populate_lists()

    def show_scheduled(self):
        tasks = self.task_manager.get_multi()
        if not self.scheduled_tasks:
            self.scheduled_tasks = tasks
            for task in tasks:
                text_to_display = f'{task.title}: {task.content}'
                widget = OneLineListItem(text=f'{text_to_display} - Due date: {task.date.date()}',
                                         font_style='H6',
                                         theme_text_color='Hint'
                                         )
                self.ids.scheduled.add_widget(widget)

    def show_today_tasks(self):
        tasks = self.task_manager.get_today_tasks()
        if not self.today_tasks:
            self.today_tasks = tasks
            for task in tasks:
                text_to_display = f'{task.title}: {task.content}'
                widget = OneLineListItem(text=f'{text_to_display} - Scheduled for TODAY',
                                         font_style='H6',
                                         theme_text_color='Hint'
                                         )
                self.ids.today_tasks.add_widget(widget)

