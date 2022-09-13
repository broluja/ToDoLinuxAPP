from kivymd.toast import toast
from kivymd.app import MDApp


class NotificationManager(object):
    """ Class for serving proper notifications, depending on platform that holds Load66App. """
    def __init__(self):
        self.app = MDApp.get_running_app()

    def __str__(self):
        return f'Notification Manager for {self.app}'

    def notify(self, text, duration=4, background=None):
        toast(text=text, duration=duration, background=background)
