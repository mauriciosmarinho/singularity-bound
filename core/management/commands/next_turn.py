from django.core.management.base import BaseCommand
from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from core.models import ResearchProject
import random
from core.models import Faction, Sector
from core.models import Leader


class Command(BaseCommand):
    help = "Avança o universo em 1 turno"

    def handle(self, *args, **kwargs):

        commander = Commander.objects.first()
        draconis = Faction.objects.filter(name="Clã Draconis").first()
        current_turn = Turn.objects.order_by("-number").first()

        next_number = current_turn.number + 1

        fuel_gain = random.randint(80, 150)
        mineral_gain = random.randint(50, 120)
        science_gain = random.randint(5, 20)

        commander.fuel += fuel_gain
        commander.minerals += mineral_gain
        commander.science += science_gain

        event_text = "========= S I N G U L A R I T Y    B O U N D =========="

        if Leader.objects.filter(name="Ministra Lyra", active=True).exists():
            commander.minerals += 30
            event_text += "\nLyra otimizou produção colonial."

        if Leader.objects.filter(name="Cientista Orion", active=True).exists():
            commander.science += 25
            event_text += "\nOrion acelerou pesquisa."

        if Leader.objects.filter(name="Almirante Vega", active=True).exists():
            commander.morale += 2
            event_text += "\nVega elevou moral das frotas."

        # =========================
        # ECONOMIA DAS COLÔNIAS
        # =========================

        economy_text = ""

        player_colonies = Sector.objects.filter(owner=commander.name).count()
        rival_colonies = Sector.objects.filter(owner="Clã Draconis").count()

        if player_colonies > 0:

            colony_minerals = player_colonies * random.randint(25, 45)
            colony_fuel = player_colonies * random.randint(10, 25)

            commander.minerals += colony_minerals
            commander.fuel += colony_fuel

            economy_text += (
                f"\nSuas colônias produziram "
                f"+{colony_minerals} minerals e "
                f"+{colony_fuel} fuel."
            )

            # chance de reputação comercial
            if random.randint(1, 100) <= 20:
                commander.reputation += 1
                economy_text += "\nRotas coloniais elevaram sua reputação."

        # rival cresce em silêncio
        if rival_colonies > 0 and draconis:
            draconis.relation -= min(2, rival_colonies // 2)


        event_text += "Setor estável. Nenhuma ocorrência extraordinária."

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

        # =========================
        # IA RIVAL
        # =========================

        rival_text = ""

        draconis = Faction.objects.filter(name="Clã Draconis").first()

        if draconis:

            action = random.choice([
                "expand",
                "military",
                "propaganda",
                "idle"
            ])

            if action == "expand":

                sector_id = random.randint(700, 999)
                sector_name = f"D-{sector_id}"

                if not Sector.objects.filter(name=sector_name).exists():
                    Sector.objects.create(
                        name=sector_name,
                        description="Colônia rival de Draconis.",
                        colonized=True,
                        owner="Clã Draconis"
                    )

                    rival_text += f"\nClã Draconis colonizou {sector_name}."

            elif action == "military":
                draconis.relation -= 2
                rival_text += "\nClã Draconis ampliou forças militares."

            elif action == "propaganda":
                commander.reputation = max(0, commander.reputation - 3)
                rival_text += "\nPropaganda rival reduziu sua reputação."

            else:
                rival_text += "\nMovimentos rivais permaneceram silenciosos."


        player_colonies = Sector.objects.filter(owner=commander.name).count()
        rival_colonies = Sector.objects.filter(owner="Clã Draconis").count()


        # =========================
        # EVENTOS RAROS
        # =========================

        rare_text = ""

        if random.randint(1, 100) <= 15:

            rare_event = random.choice([
                "ancient_ai",
                "civil_war",
                "mineral_boom",
                "solar_collapse",
                "tech_cult"
            ])

            if rare_event == "ancient_ai":
                commander.science += 120
                rare_text += (
                    "\nEvento raro: IA ancestral desperta "
                    "e compartilha conhecimento proibido."
                )

            elif rare_event == "civil_war":
                if draconis:
                    draconis.relation -= 10
                    draconis.save()

                rare_text += (
                    "\nEvento raro: guerra civil enfraqueceu Clã Draconis."
                )

            elif rare_event == "mineral_boom":
                commander.minerals += 180
                rare_text += (
                    "\nEvento raro: megadepósito mineral encontrado."
                )

            elif rare_event == "solar_collapse":
                commander.fuel = max(0, commander.fuel - 90)
                rare_text += (
                    "\nEvento raro: estrela em colapso afetou rotas energéticas."
                )

            elif rare_event == "tech_cult":
                commander.reputation += 4
                commander.morale += 4

                rare_text += (
                    "\nEvento raro: culto tecnocrático apoia seu governo."
                )


        # Junta tudo no texto final
        event_text += economy_text
        event_text += history_text
        event_text += rival_text
        event_text += rare_text
        end_text = ""

        # ======================
        # VITÓRIA
        # ======================

        if commander.reputation >= 90:
            end_text = "\n\nVITÓRIA HISTÓRICA: sua reputação unificou a galáxia."

        elif player_colonies >= 5:
            end_text = "\n\nVITÓRIA EXPANSIONISTA: seu império domina cinco colônias."

        elif draconis and draconis.relation <= -80:
            end_text = "\n\nVITÓRIA MILITAR: Clã Draconis foi neutralizado."

        # ======================
        # DERROTA
        # ======================

        elif commander.morale <= 0:
            end_text = "\n\nDERROTA: colapso social derrubou seu governo."

        elif commander.fuel <= 0:
            end_text = "\n\nDERROTA: colapso logístico encerrou a campanha."

        elif rival_colonies >= 5:
            end_text = "\n\nDERROTA: Clã Draconis dominou o setor."

        event_text += end_text

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

        if end_text:
            self.stdout.write("Campanha encerrada.")
