from django.core.management.base import BaseCommand
from core.models import Leader


class Command(BaseCommand):
    help = "Ativa um líder"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **kwargs):

        query = kwargs["name"].lower()

        leader = Leader.objects.filter(
            name__icontains=query
        ).first()

        if not leader:
            self.stdout.write("Líder não encontrado.")
            return

        leader.active = True
        leader.save()

        self.stdout.write("")
        self.stdout.write(f"{leader.name} entrou no conselho.")
        self.stdout.write("")