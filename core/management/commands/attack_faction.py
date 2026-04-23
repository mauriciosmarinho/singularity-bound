import random

from django.core.management.base import BaseCommand

from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from core.models import Fleet, Faction


class Command(BaseCommand):
    help = "Ataca uma facção com uma frota"

    def add_arguments(self, parser):
        parser.add_argument("fleet_name", type=str)
        parser.add_argument("faction_name", type=str)

    def handle(self, *args, **kwargs):

        fleet_name = kwargs["fleet_name"]
        faction_name = kwargs["faction_name"]

        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        fleet = Fleet.objects.filter(name=fleet_name).first()
        faction = Faction.objects.filter(name=faction_name).first()

        if not fleet:
            self.stdout.write("Frota inexistente.")
            return

        if not faction:
            self.stdout.write("Facção inexistente.")
            return

        if fleet.status != "Operacional":
            self.stdout.write("Frota indisponível.")
            return

        enemy_power = random.randint(70, 140)

        total = fleet.power - enemy_power + random.randint(-20, 20)

        if total >= 0:
            # vitória
            rep_gain = random.randint(3, 6)
            relation_loss = random.randint(10, 18)

            commander.reputation += rep_gain
            faction.relation -= relation_loss

            fleet.status = "Reparos"

            msg = (
                f"Vitória tática contra {faction.name}. "
                f"+{rep_gain} reputation. "
                f"Hostilidade ampliada."
            )

        else:
            # derrota
            morale_loss = random.randint(6, 12)

            commander.morale -= morale_loss
            faction.relation -= 5

            fleet.status = "Reparos"

            msg = (
                f"Derrota severa contra {faction.name}. "
                f"-{morale_loss} morale."
            )

        commander.save()
        faction.save()
        fleet.save()

        LogEntry.objects.create(
            turn=turn.number,
            message=msg
        )

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
