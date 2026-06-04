from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_roles(sender, **kwargs):
    from django.contrib.auth.models import Group
    Group.objects.get_or_create(name='Admin')
    Group.objects.get_or_create(name='Nutricionista')

class GymConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym'

    def ready(self):
        post_migrate.connect(create_roles, sender=self)
