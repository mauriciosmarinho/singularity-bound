from django.core.management.base import BaseCommand
from core.models import Fleet


class Command(BaseCommand):
    help = "Mostra frotas"

    def handle(self, *args, **kwargs):

        self.stdout.write("")
        self.stdout.write("===== FROTAS =====")
        self.stdout.write("")

        for fleet in Fleet.objects.all():
            self.stdout.write(
                f"{fleet.name:12} Poder: {fleet.power:3}   Status: {fleet.status}"
            )

        self.stdout.write("")
