from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Painel principal"

    def handle(self, *args, **kwargs):

        lines = [
            "",
            "===== SINGULARITY BOUND =====",
            "",
            "ESTADO:",
            " status_universe",
            " aura_report",
            " logs_report",
            "",
            "TEMPO:",
            " next_turn",
            "",
            "POLÍTICA:",
            " trigger_event",
            " resolve_event 1",
            " factions_report",
            "",
            "CIÊNCIA:",
            " start_research warp_drive",
            " research_status",
            "",
            "EXPANSÃO:",
            " explore_sector",
            " sectors_report",
            " colonize_sector alpha X-441",
            "",
            "MILITAR:",
            " build_fleet alpha",
            " fleets_report",
            " attack_faction alpha \"Clã Draconis\"",
            " repair_fleets",
            "",
            "ADMIN:",
            " seed_universe",
            "",
        ]

        for line in lines:
            self.stdout.write(line)