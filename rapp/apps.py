from django.apps import AppConfig


class RappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rapp'

    def ready(self):
        import rapp.signals 
        # importing inside this function, to avoid circular imports as django recommends