from django.core.management.base import BaseCommand

from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry


class Command(BaseCommand):
    help = "Investe recursos em pesquisa"

    def handle(self, *args, **kwargs):

        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        cost = 100
        gain = 25

        if commander.minerals < cost:
            self.stdout.write("")
            self.stdout.write("AURA:")
            self.stdout.write("Recursos minerais insuficientes para pesquisa.")
            self.stdout.write("")
            return

        commander.minerals -= cost
        commander.science += gain
        commander.save()

        msg = (
            f"Projeto científico autorizado. "
            f"-{cost} minerals / +{gain} science."
        )

        LogEntry.objects.create(
            turn=turn.number,
            message=msg
        )

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
