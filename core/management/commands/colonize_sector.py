from django.core.management.base import BaseCommand

from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from core.models import Fleet, Sector


class Command(BaseCommand):
    help = "Coloniza setor usando frota"

    def add_arguments(self, parser):
        parser.add_argument("fleet_name", type=str)
        parser.add_argument("sector_name", type=str)

    def handle(self, *args, **kwargs):

        fleet_name = kwargs["fleet_name"]
        sector_name = kwargs["sector_name"]

        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        fleet = Fleet.objects.filter(name=fleet_name).first()
        sector = Sector.objects.filter(name=sector_name).first()

        if not fleet:
            self.stdout.write("Frota inexistente.")
            return

        if not sector:
            self.stdout.write("Setor inexistente.")
            return

        if sector.colonized:
            self.stdout.write("Setor já colonizado.")
            return

        cost_fuel = 120

        if commander.fuel < cost_fuel:
            self.stdout.write("Fuel insuficiente.")
            return

        commander.fuel -= cost_fuel
        commander.reputation += 3
        commander.save()

        sector.colonized = True
        sector.owner = commander.name
        sector.save()

        msg = (
            f"Frota {fleet.name} estabeleceu colônia em "
            f"{sector.name}. Prestígio territorial ampliado."
        )

        LogEntry.objects.create(
            turn=turn.number,
            message=msg
        )

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
