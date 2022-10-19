from django.apps import AppConfig


class User_AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'

    def ready(self):
        import user_auth.signals