import random
from django.core.management.base import BaseCommand
from events.models import ActiveEvent


class Command(BaseCommand):
    help = "Gera evento ativo"

    def handle(self, *args, **kwargs):

        ActiveEvent.objects.all().delete()

        events = [
            (
                "Crise em Vesta-4",
                "A colônia sofre escassez crítica.\n"
                "1) Enviar suprimentos\n"
                "2) Reprimir protestos\n"
                "3) Ignorar situação"
            ),
            (
                "Mercadores de Orion",
                "Uma guilda oferece parceria.\n"
                "1) Aceitar acordo\n"
                "2) Taxar fortemente\n"
                "3) Recusar contato"
            ),
            (
                "Ruído no Horizonte",
                "Sinal desconhecido vindo da singularidade.\n"
                "1) Investigar\n"
                "2) Bloquear setor\n"
                "3) Ignorar"
            ),
        ]

        title, desc = random.choice(events)

        ActiveEvent.objects.create(
            title=title,
            description=desc
        )

        self.stdout.write("")
        self.stdout.write(f"AURA: {title}")
        self.stdout.write(desc)
        self.stdout.write("")
