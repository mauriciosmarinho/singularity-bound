import random

from django.core.management.base import BaseCommand
from core.models import Faction, Sector
from players.models import Commander


class Command(BaseCommand):
    help = "Espiona facção rival"

    def add_arguments(self, parser):
        parser.add_argument("faction_name", type=str)

    def handle(self, *args, **kwargs):

        name = kwargs["faction_name"]

        commander = Commander.objects.first()
        faction = Faction.objects.filter(name=name).first()

        if not faction:
            self.stdout.write("Facção inexistente.")
            return

        roll = random.randint(1, 100)

        self.stdout.write("")
        self.stdout.write("AURA:")

        if roll <= 60:
            sectors = Sector.objects.filter(owner=name)

            count = sectors.count()

            self.stdout.write(
                f"Agentes confirmam {count} colônias controladas por {name}."
            )

            if count > 0:
                target = sectors.order_by("?").first()
                self.stdout.write(
                    f"Atividade detectada em {target.name}."
                )

        elif roll <= 85:
            commander.reputation = max(0, commander.reputation - 2)
            commander.save()

            self.stdout.write(
                "Operação detectada. Sua reputação sofreu desgaste."
            )

        else:
            commander.morale -= 3
            commander.save()

            self.stdout.write(
                "Agentes capturados. Moral interna abalada."
            )

        self.stdout.write("")