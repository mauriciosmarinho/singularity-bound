from players.models import Commander
from turns.models import Turn

from core.services.economy import apply_income
from core.services.rival_ai import run_rival_turn

from .events import trigger_rare_event
from .victory import check_game_state


class TurnEngine:

    def run(self):

        commander = Commander.objects.first()

        if not commander:
            return "Nenhum comandante encontrado."

        fuel, minerals, science = apply_income(commander)

        turn = Turn.objects.create()

        text = (
            f"===== TURNO {turn.number} =====\n\n"
            f"AURA:\n"
            f"+{fuel} fuel\n"
            f"+{minerals} minerals\n"
            f"+{science} science"
        )

        text += run_rival_turn()
        text += trigger_rare_event(commander)
        text += check_game_state(commander)

        return text