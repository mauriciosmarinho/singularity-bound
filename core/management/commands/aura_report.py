from django.core.management.base import BaseCommand
from players.models import Commander


class Command(BaseCommand):
    help = "Relatório interpretativo da AURA"

    def handle(self, *args, **kwargs):

        commander = Commander.objects.first()

        morale = commander.morale
        reputation = commander.reputation
        science = commander.science
        fuel = commander.fuel
        minerals = commander.minerals

        messages = []

        # Moral
        if morale < 40:
            messages.append(
                "Tripulações demonstram sinais severos de desgaste psicológico."
            )
        elif morale < 70:
            messages.append(
                "Eficiência operacional moderada. Moral exige atenção."
            )
        else:
            messages.append(
                "Tripulações confiantes e disciplinadas."
            )

        # Reputação
        if reputation < 30:
            messages.append(
                "Facções externas classificam seu governo como instável."
            )
        elif reputation > 70:
            messages.append(
                "Sua liderança inspira confiança diplomática."
            )

        # Ciência
        if science > 120:
            messages.append(
                "Complexo científico ultrapassou expectativas estratégicas."
            )

        # Recursos
        if fuel < 150:
            messages.append(
                "Reservas energéticas perigosamente baixas."
            )

        if minerals > 1200:
            messages.append(
                "Capacidade industrial robusta detectada."
            )

        # Perfil geral
        if morale < 40 and minerals > 800:
            messages.append(
                "Padrão identificado: crescimento material à custa humana."
            )

        self.stdout.write("")
        self.stdout.write("===== AURA REPORT =====")
        self.stdout.write("")

        for msg in messages:
            self.stdout.write(f"- {msg}")

        self.stdout.write("")
