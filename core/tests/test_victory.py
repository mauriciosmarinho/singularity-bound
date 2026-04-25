from django.test import TestCase
from players.models import Commander
from core.services.victory import check_game_state


class VictoryTest(TestCase):

    def test_defeat_when_morale_zero(self):

        commander = Commander.objects.create(
            name="Teste",
            morale=0,
            fuel=100
        )

        result = check_game_state(commander)

        self.assertIn("DERROTA", result)