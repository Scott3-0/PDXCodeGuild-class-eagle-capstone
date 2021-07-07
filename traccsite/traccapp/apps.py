from django.apps import AppConfig


class TraccappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'traccapp'
    verbose_name = "Tracc App"
    default_app_config = 'traccapp.apps.TraccappConfig'