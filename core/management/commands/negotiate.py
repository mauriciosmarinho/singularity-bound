from django.core.management.base import BaseCommand
from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry


class Command(BaseCommand):
    help = "Negociação diplomática"

    def handle(self, *args, **kwargs):
        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        cost = 80
        gain = 6

        if commander.fuel < cost:
            self.stdout.write("AURA: combustível insuficiente.")
            return

        commander.fuel -= cost
        commander.reputation += gain
        commander.save()

        msg = f"Negociação concluída. -{cost} fuel / +{gain} reputation."

        LogEntry.objects.create(turn=turn.number, message=msg)

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
