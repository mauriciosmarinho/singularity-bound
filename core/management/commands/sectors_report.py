from django.core.management.base import BaseCommand
from core.models import Sector


class Command(BaseCommand):
    help = "Mostra setores descobertos"

    def handle(self, *args, **kwargs):

        self.stdout.write("")
        self.stdout.write("===== SETORES =====")
        self.stdout.write("")

        for sector in Sector.objects.all():

            status = "Colonizado" if sector.colonized else "Livre"

            self.stdout.write(
                f"{sector.name:10} {status:12} {sector.description}"
            )

        self.stdout.write("")
