from django.apps import AppConfig


class NewloginConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "newlogin"
    def ready(self):
        import newlogin.signals
