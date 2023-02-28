import random


def dice_value():
    return random.randint(1, 6)


def five_dices_values():
    dices_values = []
    for i in range(5):
        dices_values.append(dice_value())
    return dices_values


