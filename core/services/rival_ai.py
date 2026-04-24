import random

from core.models import Faction


def run_rival_turn():

    draconis = Faction.objects.filter(
        name="Clã Draconis"
    ).first()

    if not draconis:
        return ""

    roll = random.randint(1, 100)

    if roll <= 35:
        draconis.power += 5
        draconis.save()
        return "\nClã Draconis ampliou forças militares."

    elif roll <= 60:
        draconis.relation -= 2
        draconis.save()
        return "\nClã Draconis iniciou propaganda hostil."

    return ""