import random


def trigger_rare_event(commander):

    if random.randint(1, 100) > 15:
        return ""

    events = [
        "ai",
        "minerals",
        "collapse",
        "cult",
    ]

    chosen = random.choice(events)

    if chosen == "ai":
        commander.science += 100
        commander.save()
        return "\nEvento raro: IA ancestral compartilhou conhecimento."

    elif chosen == "minerals":
        commander.minerals += 150
        commander.save()
        return "\nEvento raro: megadepósito mineral descoberto."

    elif chosen == "collapse":
        commander.fuel = max(0, commander.fuel - 80)
        commander.save()
        return "\nEvento raro: colapso estelar afetou rotas."

    elif chosen == "cult":
        commander.reputation += 3
        commander.save()
        return "\nEvento raro: culto tecnocrático apoia seu governo."

    return ""