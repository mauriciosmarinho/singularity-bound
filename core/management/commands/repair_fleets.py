from django.core.management.base import BaseCommand
from core.models import Fleet


class Command(BaseCommand):
    help = "Repara todas as frotas"

    def handle(self, *args, **kwargs):

        for fleet in Fleet.objects.all():
            fleet.status = "Operacional"
            fleet.save()

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write("Todas as frotas retornaram ao serviço.")
        self.stdout.write("")
