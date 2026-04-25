from django.test import TestCase
from players.models import Commander
from core.services.economy import apply_income


class EconomyTest(TestCase):

    def test_income_increases_resources(self):

        commander = Commander.objects.create(
            name="Teste",
            fuel=100,
            minerals=100,
            science=100
        )

        apply_income(commander)

        commander.refresh_from_db()

        self.assertGreater(commander.fuel, 100)
        self.assertGreater(commander.minerals, 100)
        self.assertGreater(commander.science, 100)