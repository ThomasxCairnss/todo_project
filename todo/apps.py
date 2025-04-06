from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'

class TodoConfig(AppConfig):
    name = 'todo'

    def ready(self):
        import todo.signals  

class TodoConfig(AppConfig):
    name = 'todo'

    def ready(self):
        import todo.signals