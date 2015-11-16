from django.apps import AppConfig


class FredslistConfig(AppConfig):
    name = 'fredslist'
    verbose_name = 'Fredslist Application'

    def ready(self):
        import fredslist.signals
