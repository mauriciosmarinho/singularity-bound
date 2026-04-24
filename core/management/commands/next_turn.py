from django.core.management.base import BaseCommand
from core.services.turn_engine import TurnEngine


class Command(BaseCommand):
    help = "Avança o turno"

    def handle(self, *args, **kwargs):

        engine = TurnEngine()
        result = engine.run()

        self.stdout.write("")
        self.stdout.write(result)
        self.stdout.write("")