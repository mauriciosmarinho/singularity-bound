from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Painel principal"

    def handle(self, *args, **kwargs):

        self.stdout.write("")
        self.stdout.write("===== SINGULARITY BOUND =====")
        self.stdout.write("")
        self.stdout.write("Comandos principais:")
        self.stdout.write("")
        self.stdout.write("status_universe")
        self.stdout.write("next_turn")
        self.stdout.write("aura_report")
        self.stdout.write("trigger_event")
        self.stdout.write("resolve_event 1")
        self.stdout.write("factions_report")
        self.stdout.write("invest_science")
        self.stdout.write("emergency_mining")
        self.stdout.write("negotiate")
        self.stdout.write("risky_slingshot")
        self.stdout.write("seed_universe")
        self.stdout.write("")
