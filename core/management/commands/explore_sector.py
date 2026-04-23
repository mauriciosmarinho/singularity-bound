import random

from django.core.management.base import BaseCommand

from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from core.models import Sector


class Command(BaseCommand):
    help = "Explora um novo setor"

    def handle(self, *args, **kwargs):

        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        sector_id = random.randint(100, 999)
        sector_name = f"X-{sector_id}"

        outcomes = [
            "rich_world",
            "ruins",
            "pirates",
            "anomaly",
            "empty"
        ]

        result = random.choice(outcomes)

        text = ""

        if result == "rich_world":
            commander.minerals += 180
            text = f"Planeta rico encontrado em {sector_name}. +180 minerals."
            desc = "Mundo mineral abundante."

        elif result == "ruins":
            commander.science += 60
            text = f"Ruínas antigas encontradas em {sector_name}. +60 science."
            desc = "Estruturas precursoras em ruínas."

        elif result == "pirates":
            commander.fuel -= 120
            text = f"Emboscada pirata em {sector_name}. -120 fuel."
            desc = "Zona hostil com atividade pirata."

        elif result == "anomaly":
            commander.reputation += 4
            text = f"Anomalia rara catalogada em {sector_name}. +4 reputation."
            desc = "Fenômeno espacial incomum."

        else:
            text = f"{sector_name} explorado. Nenhum recurso relevante."
            desc = "Setor vazio."

        commander.save()

        Sector.objects.create(
            name=sector_name,
            description=desc
        )

        LogEntry.objects.create(
            turn=turn.number,
            message=text
        )

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(text)
        self.stdout.write("")
