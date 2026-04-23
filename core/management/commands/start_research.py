from django.core.management.base import BaseCommand
from core.models import ResearchProject


class Command(BaseCommand):
    help = "Inicia pesquisa"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **kwargs):

        name = kwargs["name"]

        active = ResearchProject.objects.filter(completed=False).first()

        if active:
            self.stdout.write("Já existe pesquisa em andamento.")
            return

        ResearchProject.objects.create(
            name=name,
            turns_remaining=3
        )

        self.stdout.write("")
        self.stdout.write(f"Pesquisa iniciada: {name}")
        self.stdout.write("Conclusão estimada: 3 turnos")
        self.stdout.write("")
