import random


def apply_income(commander):

    fuel_gain = random.randint(40, 90)
    mineral_gain = random.randint(60, 120)
    science_gain = random.randint(20, 50)

    commander.fuel += fuel_gain
    commander.minerals += mineral_gain
    commander.science += science_gain
    commander.save()

    return (
        fuel_gain,
        mineral_gain,
        science_gain,
    )