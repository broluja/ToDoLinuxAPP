from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

from View.Managers.notification_manager import NotificationManager
from Model.repository.task_repository import task_repository
from Model.repository.list_repository import list_repository


class CardDialogContent(MDBoxLayout):
    """Dialog box for creating a new list."""
    def __init__(self, **kwargs):
        super(CardDialogContent, self).__init__(**kwargs)
        self.list_manager = list_repository
        self.notifier = NotificationManager()

    def create_list(self):
        list_name = self.ids.list_field.text
        if not list_name:
            self.notifier.notify('Please enter a name for the list.')
            return
        try:
            self.list_manager.create({'name': list_name})
        except Exception as e:
            print(e)


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    """Implements a material design v3 card."""
    text = StringProperty()
    tasks = StringProperty('No tasks.')
    elevation = 4.0


class CardScreenView(MDScreen):
    """View of the lists in form of Material design V3 card."""
    lists = ListProperty()
    selected = StringProperty()
    list_creation_box = ObjectProperty()

    def __init__(self, **kwargs):
        super(CardScreenView, self).__init__(**kwargs)
        self.task_manager = task_repository
        self.list_manager = list_repository
        self.get_lists()

    def on_enter(self, *args):
        self.populate_lists()
        self.refresh_lists()

    def get_lists(self):
        try:
            lists = self.list_manager.get_multi()
            for created_list in lists:
                self.lists.append({'ID': created_list.id, 'Name': created_list.name, 'Populated': False})
        except Exception as e:
            print(e)

    def populate_lists(self):
        for table in self.lists:
            if not table['Populated']:
                tasks = self.task_manager.get_tasks_by_list_id(table['ID'])
                label_text = ''.join((str(task.title) + '\n') for task in tasks)
                widget = MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style='elevated',
                    text=table['Name'],
                    tasks=label_text,
                    on_touch_down=lambda x, y: self.select_list(x, y)
                )
                widget.id = table['Name']
                table['Populated'] = True
                self.ids.listing.add_widget(widget)

    def select_list(self, widget, touch):
        self.selected = widget.text
        self.manager.switch_screen('main', selected_list=self.selected)

    def open_dialog(self):
        dialog = MDDialog(
            pos_hint={'center_x': .2, 'top': .9},
            title='Create new List',
            type='custom',
            content_cls=CardDialogContent()
        )
        self.list_creation_box = dialog
        self.list_creation_box.open()

    def refresh_lists(self):
        self.ids.listing.clear_widgets(self.ids.listing.children)
        self.get_lists()
        self.populate_lists()
