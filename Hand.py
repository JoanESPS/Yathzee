from Dice import Dice


class Hand:
    def __init__(self):
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice()]

    def roll_dices(self):
        for dice in self.dices:
            dice.roll_dice()
