from django.core.management.base import BaseCommand
from core.models import Faction


class Command(BaseCommand):
    help = "Mostra facções"

    def handle(self, *args, **kwargs):

        self.stdout.write("")
        self.stdout.write("===== FACÇÕES =====")
        self.stdout.write("")

        for faction in Faction.objects.all():
            self.stdout.write(
                f"{faction.name:20} Relação: {faction.relation:3} ({faction.mood()})"
            )

        self.stdout.write("")
