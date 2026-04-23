import random

from django.core.management.base import BaseCommand
from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from core.models import Fleet


class Command(BaseCommand):
    help = "Constrói nova frota"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **kwargs):

        name = kwargs["name"]

        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        cost_fuel = 180
        cost_minerals = 220

        if commander.fuel < cost_fuel or commander.minerals < cost_minerals:
            self.stdout.write("")
            self.stdout.write("AURA:")
            self.stdout.write("Recursos insuficientes para nova frota.")
            self.stdout.write("")
            return

        if Fleet.objects.filter(name=name).exists():
            self.stdout.write("Já existe frota com esse nome.")
            return

        commander.fuel -= cost_fuel
        commander.minerals -= cost_minerals
        commander.save()

        power = random.randint(80, 140)

        Fleet.objects.create(
            name=name,
            power=power,
            status="Operacional"
        )

        msg = f"Frota {name} lançada ao serviço. Poder militar {power}."

        LogEntry.objects.create(
            turn=turn.number,
            message=msg
        )

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
