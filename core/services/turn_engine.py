import random

from players.models import Commander
from turns.models import Turn


class TurnEngine:

    def run(self):

        commander = Commander.objects.first()

        if not commander:
            return "Nenhum comandante encontrado."

        fuel_gain = random.randint(40, 90)
        mineral_gain = random.randint(60, 120)
        science_gain = random.randint(20, 50)

        commander.fuel += fuel_gain
        commander.minerals += mineral_gain
        commander.science += science_gain

        commander.save()

        turn = Turn.objects.create()

        return (
            f"===== TURNO {turn.number} =====\n\n"
            f"AURA:\n"
            f"+{fuel_gain} fuel\n"
            f"+{mineral_gain} minerals\n"
            f"+{science_gain} science\n"
        )