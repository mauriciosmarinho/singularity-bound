import random
from django.core.management.base import BaseCommand
from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry


class Command(BaseCommand):
    help = "Extração emergencial de minérios"

    def handle(self, *args, **kwargs):
        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        gain = random.randint(120, 250)
        morale_loss = random.randint(5, 12)

        commander.minerals += gain
        commander.morale -= morale_loss
        commander.save()

        msg = f"Mineração emergencial autorizada. +{gain} minerals / -{morale_loss} morale."

        LogEntry.objects.create(turn=turn.number, message=msg)

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
