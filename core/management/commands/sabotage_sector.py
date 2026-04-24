import random

from django.core.management.base import BaseCommand
from core.models import Sector
from players.models import Commander


class Command(BaseCommand):
    help = "Sabota setor rival"

    def add_arguments(self, parser):
        parser.add_argument("sector_name", type=str)

    def handle(self, *args, **kwargs):

        name = kwargs["sector_name"]

        commander = Commander.objects.first()

        sector = Sector.objects.filter(name=name).first()

        if not sector:
            self.stdout.write("Setor inexistente.")
            return

        if sector.owner != "Clã Draconis":
            self.stdout.write("Sabotagem só pode atingir setor rival.")
            return

        roll = random.randint(1, 100)

        self.stdout.write("")
        self.stdout.write("AURA:")

        if roll <= 55:
            sector.colonized = False
            sector.owner = ""
            sector.save()

            self.stdout.write(
                f"Sabotagem bem-sucedida. {name} entrou em colapso."
            )

        elif roll <= 80:
            commander.reputation = max(0, commander.reputation - 3)
            commander.save()

            self.stdout.write(
                "Operação exposta diplomaticamente."
            )

        else:
            commander.morale -= 5
            commander.save()

            self.stdout.write(
                "Fracasso total. Agentes perdidos."
            )

        self.stdout.write("")