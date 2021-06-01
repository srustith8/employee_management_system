from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
class EmsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emsapp'
class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"

