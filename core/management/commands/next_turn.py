import random

from django.core.management.base import BaseCommand

from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from core.models import ResearchProject
from core.models import Faction, Sector


class Command(BaseCommand):
    help = "Avança o universo em 1 turno"

    def handle(self, *args, **kwargs):

        commander = Commander.objects.first()
        current_turn = Turn.objects.order_by("-number").first()

        next_number = current_turn.number + 1

        fuel_gain = random.randint(80, 150)
        mineral_gain = random.randint(50, 120)
        science_gain = random.randint(5, 20)

        commander.fuel += fuel_gain
        commander.minerals += mineral_gain
        commander.science += science_gain

        event_text = "Setor estável. Nenhuma ocorrência extraordinária."

        roll = random.randint(1, 100)

        if roll <= 25:
            # crise
            loss = random.randint(20, 80)
            commander.minerals -= loss
            commander.morale -= 5
            event_text = f"CRISE: motim industrial reduziu {loss} minerals."

        elif roll <= 50:
            # oportunidade
            gain = random.randint(50, 150)
            commander.fuel += gain
            commander.reputation += 3
            event_text = f"OPORTUNIDADE: rota comercial gerou +{gain} fuel."

        project = ResearchProject.objects.filter(completed=False).first()

        if project:
            project.turns_remaining -= 1

            if project.turns_remaining <= 0:
                project.completed = True
                event_text += f" \n Pesquisa concluída: {project.name}."
            project.save()
        
        history_text = ""
        
        # 1. Moral baixa gera greve
        if commander.morale <= 40:
            commander.minerals = max(0, commander.minerals - 80)
            history_text += "\nGreves internas reduziram produção mineral."

        # 2. Reputação baixa gera isolamento
        if commander.reputation <= 25:
            commander.fuel = max(0, commander.fuel - 60)
            history_text += "\nSanções externas afetaram rotas comerciais."

        # 3. Facção hostil pode retaliar
        hostile = Faction.objects.filter(relation__lt=25).first()

        if hostile:
            commander.fuel = max(0, commander.fuel - 90)
            history_text += f"\n{hostile.name} executou retaliação estratégica."

        # 4. Expansão excessiva assusta vizinhos
        colonies = Sector.objects.filter(colonized=True).count()

        if colonies >= 3:
            for faction in Faction.objects.all():
                faction.relation -= 3
                faction.save()

            history_text += "\nSua expansão territorial alarmou facções vizinhas."
            event_text += history_text

        commander.save()

        Turn.objects.create(number=next_number)

        LogEntry.objects.create(
            turn=next_number,
            message=event_text
        )

        self.stdout.write("")
        self.stdout.write(f"===== TURNO {next_number} =====")
        self.stdout.write("")
        self.stdout.write(f"+ Fuel Base     : {fuel_gain}")
        self.stdout.write(f"+ Minerals Base : {mineral_gain}")
        self.stdout.write(f"+ Science Base  : {science_gain}")
        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(event_text)
        self.stdout.write("")
