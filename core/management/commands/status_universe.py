from django.core.management.base import BaseCommand
from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry


class Command(BaseCommand):
    help = "Mostra o estado atual do universo"

    def handle(self, *args, **kwargs):
        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()
        log = LogEntry.objects.order_by("-created_at").first()

        self.stdout.write("")
        self.stdout.write("===== SINGULARITY BOUND =====")
        self.stdout.write("")

        self.stdout.write(f"Comandante : {commander.name}")
        self.stdout.write(f"Turno      : {turn.number}")
        self.stdout.write("")

        self.stdout.write("Recursos")
        self.stdout.write(f"  Fuel     : {commander.fuel}")
        self.stdout.write(f"  Minerals : {commander.minerals}")
        self.stdout.write(f"  Science  : {commander.science}")
        self.stdout.write("")

        self.stdout.write("Estado")
        self.stdout.write(f"  Morale   : {commander.morale}")
        self.stdout.write(f"  Reputation : {commander.reputation}")
        self.stdout.write("")

        self.stdout.write("AURA LOG")
        self.stdout.write(f"  {log.message}")
        self.stdout.write("")
