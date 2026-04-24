from django.core.management.base import BaseCommand
from core.models import Leader


class Command(BaseCommand):
    help = "Mostra conselho imperial"

    def handle(self, *args, **kwargs):

        self.stdout.write("")
        self.stdout.write("===== CONSELHO IMPERIAL =====")
        self.stdout.write("")

        for leader in Leader.objects.all():
            status = "Ativo" if leader.active else "Inativo"

            self.stdout.write(
                f"{leader.name:20} {status:10} {leader.bonus}"
            )

        self.stdout.write("")