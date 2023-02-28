import random


class Dice:
    def __init__(self, value=1):
        self.value = value

    def roll_dice(self):
        self.value = random.randint(1, 6)
