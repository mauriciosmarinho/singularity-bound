from django.core.management.base import BaseCommand
from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from events.models import ActiveEvent
from core.models import Faction


class Command(BaseCommand):
    help = "Resolve evento ativo"

    def add_arguments(self, parser):
        parser.add_argument("choice", type=int)

    def handle(self, *args, **kwargs):

        choice = kwargs["choice"]

        event = ActiveEvent.objects.first()

        if not event:
            self.stdout.write("AURA: nenhum evento ativo.")
            return

        commander = Commander.objects.first()
        turn = Turn.objects.order_by("-number").first()

        msg = ""

        if event.title == "Crise em Vesta-4":

            vesta, _ = Faction.objects.get_or_create(name="Coalizão Vesta")

            if choice == 1:
                commander.fuel -= 100
                commander.reputation += 5
                vesta.relation += 10
                vesta.save()
                msg = "Suprimentos enviados. Coalizão Vesta agradecida."

            elif choice == 2:
                commander.minerals += 80
                commander.morale -= 10
                vesta.relation -= 12
                vesta.save()
                msg = "Protestos reprimidos. Relações com Vesta pioraram."

            else:
                commander.reputation -= 8
                vesta.relation -= 8
                vesta.save()
                msg = "Crise ignorada. Vesta perdeu confiança."

        else:
            if choice == 1:
                commander.science += 20
                msg = "Decisão ousada executada."
            elif choice == 2:
                commander.reputation += 2
                msg = "Resposta conservadora aplicada."
            else:
                commander.morale -= 3
                msg = "Nada foi feito."

        commander.save()

        LogEntry.objects.create(
            turn=turn.number,
            message=f"{event.title}: {msg}"
        )

        event.delete()

        self.stdout.write("")
        self.stdout.write("AURA:")
        self.stdout.write(msg)
        self.stdout.write("")
