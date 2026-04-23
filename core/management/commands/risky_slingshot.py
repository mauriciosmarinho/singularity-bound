import random
from django.core.management.base import BaseCommand
from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry


class Command(BaseCommand):
    help = "Manobra arriscada ao redor de singularidade"

    def handle(self, *args, **kwargs):
        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        roll = random.randint(1, 100)

        if roll <= 70:
            gain = random.randint(150, 300)
            commander.fuel += gain
            commander.reputation += 2
            msg = f"Slingshot bem-sucedido. +{gain} fuel."

        else:
            morale_loss = random.randint(10, 20)
            commander.morale -= morale_loss
            commander.reputation -= 4
            msg = f"Falha crítica no horizonte de eventos. -{morale_loss} morale."

        commander.save()

        LogEntry.objects.create(turn=turn.number, message=msg)

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
