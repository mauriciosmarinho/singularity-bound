from django.core.management.base import BaseCommand
from core.models import Sector


class Command(BaseCommand):
    help = "Mostra presença rival conhecida"

    def handle(self, *args, **kwargs):

        self.stdout.write("")
        self.stdout.write("===== INTELIGÊNCIA =====")
        self.stdout.write("")

        rivals = Sector.objects.filter(owner="Clã Draconis")

        if rivals.exists():
            for sector in rivals:
                self.stdout.write(
                    f"{sector.name:10} Base rival detectada"
                )
        else:
            self.stdout.write("Nenhuma presença rival detectada.")

        self.stdout.write("")