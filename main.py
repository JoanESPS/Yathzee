import random
from Hand import Hand


hand = Hand()
hand.roll_dices()


def sum_of_ones(player_hand):
    score = 0
    for dice in player_hand:
        if dice.value == 1:
            score += dice.value
    return score


def sum_of_twos(player_hand):
    score = 0
    for dice in player_hand:
        if dice.value == 2:
            score += dice.value
    return score