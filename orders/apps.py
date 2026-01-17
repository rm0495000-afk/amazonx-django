# amazon/apps.py
from django.apps import AppConfig

class AmazonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "amazon"

    def ready(self):
        from django.core.management import call_command
        try:
            call_command("loaddata", "products", verbosity=0)
        except Exception:
            pass
