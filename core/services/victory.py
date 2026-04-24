from core.models import Sector


def check_game_state(commander):

    colonies = Sector.objects.filter(
        owner="Império Humano"
    ).count()

    if colonies >= 5:
        return "\nVITÓRIA: Domínio territorial alcançado."

    if commander.morale <= 0:
        return "\nDERROTA: Moral do império colapsou."

    if commander.fuel <= 0:
        return "\nDERROTA: Crise logística total."

    return ""