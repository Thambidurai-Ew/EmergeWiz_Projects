from django.apps import AppConfig


class EwizAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ewiz_app'

    def ready(self):
        import Ewiz_app.signals