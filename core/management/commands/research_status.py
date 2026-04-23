from django.core.management.base import BaseCommand
from core.models import ResearchProject


class Command(BaseCommand):
    help = "Mostra status da pesquisa"

    def handle(self, *args, **kwargs):

        project = ResearchProject.objects.filter(completed=False).first()

        self.stdout.write("")

        if not project:
            self.stdout.write("Nenhuma pesquisa ativa.")
        else:
            self.stdout.write(f"Projeto: {project.name}")
            self.stdout.write(
                f"Turnos restantes: {project.turns_remaining}"
            )

        self.stdout.write("")
