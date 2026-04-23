from django.core.management.base import BaseCommand

from players.models import Commander
from turns.models import Turn
from logs.models import LogEntry
from core.models import Faction
from events.models import ActiveEvent


class Command(BaseCommand):
    help = "Reinicia e popula o universo"

    def handle(self, *args, **kwargs):

        # limpar dados
        ActiveEvent.objects.all().delete()
        LogEntry.objects.all().delete()
        Turn.objects.all().delete()
        Commander.objects.all().delete()
        Faction.objects.all().delete()

        # comandante
        Commander.objects.create(
            name="Comandante",
            fuel=1000,
            minerals=500,
            science=0,
            morale=100,
            reputation=50
        )

        # turno inicial
        Turn.objects.create(number=1)

        # facções
        Faction.objects.create(name="Sindicato de Orion", relation=55)
        Faction.objects.create(name="Coalizão Vesta", relation=50)
        Faction.objects.create(name="Clã Draconis", relation=35)

        # log inicial
        LogEntry.objects.create(
            turn=1,
            message="AURA online. Nova campanha iniciada."
        )

        self.stdout.write("")
        self.stdout.write("Universo reiniciado com sucesso.")
        self.stdout.write("")
